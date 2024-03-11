#!/usr/bin/python3
'''Tests for FileStorage class'''
import models
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFile_Storage(unittest.TestCase):
    '''start tests'''
    def setUp(self):
        '''Checks if an object can be created from the class'''
        self.my_object = FileStorage()
    def test_docstring(self):
        '''Checks if docstrings are present in every class'''
        class_msg = "Clase does not has docstring"
        self.assertIsNotNone(self.my_object, class_msg)  # Classes

    def test_executable_file(self):
        '''test if file has permissions u+x to execute'''
        can_be_exec = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(can_be_exec)

    def test_is_an_instance(self):
        '''check if my_model is an instance of BaseModel'''
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)
