from datetime import datetime
from app import db


class SerializableModel(object):
    def to_dict(self):
        value = {}
        for column in self.__table__.columns:
            attribute = getattr(self, column.name)
            if isinstance(attribute, datetime):
                attribute = str(attribute)
            value[column.name] = attribute
        return value


class Links(db.Model, SerializableModel):
    __tablename__ = 'Links'

    Id = db.Column(db.String, primary_key=True)
    Link = db.Column(db.String)
    ApiKey = db.Column(db.String)
    DateCreated = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, Id, Link, ApiKey):
        self.Id = Id
        self.Link = Link
        self.ApiKey = ApiKey

