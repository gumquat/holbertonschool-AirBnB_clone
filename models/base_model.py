#!/usr/bin/python3
""" a class that defines all common attributes/methods for other classes """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ the base class for all other classes in this project """
    def __init__(self, *args, **kwargs):
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.save()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat("T", "microseconds")
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat("T", "microseconds")
        return obj_dict
