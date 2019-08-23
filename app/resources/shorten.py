from flask import Response, abort, request
from flask_restful import Resource
from hashlib import sha1
from json import dumps
from app import app, db
from app.persist.models import Links

class Shorten(Resource):
    def post(self):
        api_key = request.values.get('api_key', None)
        link = request.values.get('link', None)

        if api_key in app.config['API_KEY_CSV'].split(','):
            if link:
                new_link = Links.query.filter(Links.Link==link).first()
                if not new_link:
                    short_hash_len = app.config['SHORT_HASH_LEN_DEFAULT']
                    full_hash = sha1(link).hexdigest()

                    while Links.query.filter(Links.Id==full_hash[:short_hash_len]).first():
                        short_hash_len += 1

                    new_link = Links(full_hash[:short_hash_len], link, api_key)
                    db.session.add(new_link)
                    db.session.commit()

                return Response(dumps(new_link.to_dict()),
                                status=200,
                                mimetype='application/json')
            abort(400)
        abort(401)

