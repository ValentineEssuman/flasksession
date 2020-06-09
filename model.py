from sqlalchemy import Column
from db import db, Serializer


class  Hero(db.Model, Serializer):
    __tablename__ = "hero"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)

   # __table_args__ = {'schema': 'public'}

    def __repr__(self):
        return '<Hero %r>' % self.name