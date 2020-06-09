
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.attributes import instance_state

db = SQLAlchemy()

class Serializer(object):

  def serialize(self, ignore=[]):
    d = list(instance_state(self).unloaded)
    return {c: None if (c in d or c in ignore) else (getattr(self, c).serialize() if issubclass(type(getattr(self, c)), db.Model) else getattr(self, c)) for c in inspect(self).attrs.keys()}

  @staticmethod
  def serialize_list(l):
    return [m.serialize() if m is not None else {} for m in l]