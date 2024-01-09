#!/usr/bin/python3
"""Contians class FileStorage"""


import os
import json


class FileStorage:
    """Serializes json file to instances and vice-versa """

    __file_path = "file.json"
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
                json.dump(self.__objects, fp)

    def reload(self):
        """Deserializes the JSON file to __objects if file-path exists """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as fp:
                try:
                    self.__objects = json.load(fp)
                except Exception as e:
                    pass
