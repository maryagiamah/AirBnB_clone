#!/usr/bin/python3
"""Contians class FileStorage"""

import models
from models.base_model import BaseModel
import os
import json


class FileStorage:
    """Serializes json file to instances and vice-versa """

    __file_path = "file.json"
    class_dict = {"BaseModel": BaseModel}
    __objects = {}

    def all(self):
        """Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id """
        k = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj.to_dicts()

    def save(self):
        """serializes __objects to the JSON file """
        with open(self.__file_path, 'w') as fp:
                json.dump(self.__objects, fp)

    def reload(self):
        """Deserializes the JSON file to __objects if file-path exists """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as fp:
                try:
                    file_dict = json.load(f)
                    for k, v in new_obj_dict.items():
                        obj = self.class_dict[v['__class__']](**v)
                        self.__objects[k] = obj
                except Exception as e:
                    pass
