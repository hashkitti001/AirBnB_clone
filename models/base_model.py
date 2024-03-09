#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime as dt


class BaseModel:
    """A class that defines all common attributes/methods
    for other classes in the AirBnB console project."""
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class
        Attributes:
               id (str): Unique identifier for the instance
               created_at (datetime): Date and time for
               when the instance is created
               updated_at (datetime): Date and time for
               when the instance is updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, dt.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid4())
            if 'created_at' not in kwargs:
                self.created_at = dt.now()
            if 'updated_at' not in kwargs:
                self.updated_at = dt.now()
        else:
            self.id = str(uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
        if not kwargs or 'id' not in kwargs:
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance

        Returns:
            str: A formatted string containing
            the class name, id and a dictionary
            representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the updated_at public attribute"""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object
        Returns:
            dict: A dictionary representation of the object
            containing the __class__, created_at, updated_at
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
