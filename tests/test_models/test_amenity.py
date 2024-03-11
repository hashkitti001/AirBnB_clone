#!/usr/bin/python3
'''Tests for User class'''
import datetime
import unittest
from models import amenity
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os
class TestAmenity(unittest.TestCase):
    '''start tests'''

    def setUp(self):
        '''Checks if an object can be created from the class'''
        self.my_object = Amenity()

    def test_docStringsExist(self):
        '''Checks if docstrings are present in every class'''
        class_msg = "Class doesn't have a docstring"
        self.assertIsNotNone(Amenity.__doc__, class_msg)
        meth_msg = "Method doesn't have a docstring"
        
    def test_instancehasid(self):
        '''Checks if the instance of the User class has an id'''
        self.assertIsNotNone(self.my_object.id)
    
    def test_idisunique(self):
        '''Checks if the id on an objects is unique (differs from another)'''
        inst_two = Amenity()
        self.assertNotEqual(self.my_object.id, inst_two.id)
    
    def test_iscorrecttype(self):
        '''Checks if the attributes of the User object are the right data type'''
        working_obj = self.my_object
        self.assertIs(type(working_obj.id), str)
        self.assertIs(type(working_obj.created_at), datetime.datetime)
        self.assertIs(type(working_obj.updated_at), datetime.datetime)
        self.assertIs(type(working_obj.name), str)
    
    def test_save(self):
        '''check if the attribute updated_at (date) is updated for
        the same object with the current date'''
        first_updated = self.my_object.updated_at
        self.my_object.save()
        second_updated = self.my_object.updated_at
        self.assertNotEqual(first_updated, second_updated)
        os.remove("file.json")
    
    def test_executable_file(self):
        '''test if file has permissions u+x to execute'''
        can_be_exec = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(can_be_exec)

    def test_to_dict(self):
        '''check if to_dict returns a dictionary, if add a class
        key with class name of the object and if updated_at and
        created_at are converted to string object in ISO format.'''
        my_dict_model = self.my_object.to_dict()
        self.assertIsInstance(my_dict_model, dict)
        for key, value in my_dict_model.items():
            flag = 0
            if my_dict_model['__class__'] == 'Amenity':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)

    def test_kwargs(self):
        '''check when a dictionary in sent as **kwargs argument'''
        self.my_object.name = "Electricity"
        self.my_object.my_number = 192
        my_object_json = self.my_object.to_dict()
        my_object_kwargs = Amenity(**my_object_json)
        self.assertNotEqual(my_object_kwargs, self.my_object)

    def test_des_and_serialization(self):
        '''check serialization and deserialization'''
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict, "a dictionary")  # Test all
        self.my_object.name = "Plummage"
        self.my_object.my_number = 3599
        self.my_object.save()
        with open("file.json", "r", encoding='utf-8') as f:
            self.assertTrue(self.my_object.name in f.read())  # Test save
if __name__ == "__main__":
    unittest.main()
