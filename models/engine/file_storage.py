#!/usr/bin/python3
"""Contians class FileStorage"""

import models
from models.base_model import BaseModel
import os
import json


class FileStorage:
    """Serializes json file to instances and vice-versa """

    __file_path = "file.json"
    class_dict = {"BaseModel": BaseModel, "User": User}
    __objects = {}

    def all(self):
        """Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id """
        k = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file """
        with open(self.__file_path, 'w') as fp:
                json.dump({k: v.to_dict() for k, v in self.__objects.items()
                       }, fp)

    def reload(self):
        """Deserializes the JSON file to __objects if file-path exists """
        try:
            with open(self.__file_path, 'r') as fp:
                    file_dict = json.load(fp)
            for k, v in file_dict.items():
                obj = self.class_dict[v['__class__']](**v)
                self.__objects[k] = obj
        except Exception as e:
            pass
