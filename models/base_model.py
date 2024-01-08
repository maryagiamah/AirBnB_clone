#!/usr/bin/python3
"""Module that contains BaseModle class """

import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """Defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """Constructor for instance attr """
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == "id":
                        setattr(self, k, str(id))
                    if k in ['created_at', 'updated_at']:
                        v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Modifies how its printed"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary of __dict__ of instance"""
        new_dict = {}
        for k, v in self.__dict__.items():
            new_dict[k] = v
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
