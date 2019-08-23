import json
from flask import abort, redirect
from flask_restful import Resource
from app.persist.models import Links


class Goto(Resource):
    def get(self, short_hash):
        redirect_link = Links.query.filter(Links.Id==short_hash).first()
        if redirect_link:
            return redirect(redirect_link.Link, 301)
        abort(404)

