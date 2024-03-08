#!/usr/bin/env python3
from models.base_model import BaseModel
import json
import os
class FileStorage:
    """A class that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = './file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary objects"""
        return self.__objects
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
        """ Serializes __objects = {}"""
        new_entry = {}
        with open(self.__file_path, mode="w") as file:
            for key, value in self.__objects.items():
                new_entry[key] = value.to_dict()
                """JSON encoder and decoder"""
            json.dump(new_entry, file)

    def reload(self):
        """ Deserializes __objects = {}"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r") as file:
                for key, value in json.load(file).items():
                    new_obj = eval(value["__class__"])(**value)
                    self.__objects[key] = new_obj
