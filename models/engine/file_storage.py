#!/usr/bin/env python3
from base_model import BaseModel
import json

class FileStorage:
    """A class that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary objects"""
        return self.__objects
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
        """Serializes __objects to the JSON file path"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        try:
            if(self.__file_path is not None):
               with open(self.__file_path, 'w', encoding='utf-8') as file:
                   json.dump(serialized_objects, file)
        except PermissionError:
            print("Access denied. Check file permissions")
        except FileNotFoundError:
            print("This file doesn't exist on this drive. Check the file path")
        except IsADirectoryError:
            print("Path leads to a directory, not a file")
        except OSError:
            print("There is no space left on your drive")
    def reload(self):
       if(self.__file_path is not None):
           with open(self.__file_path, 'r', encoding='utf-8') as file:
               data = json.load(file)
       else:
           return
           