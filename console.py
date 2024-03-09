from ast import arg
import cmd
import os
import sys

from models.base_model import BaseModel
import models
import json

class HBNBCommand(cmd.Cmd):
    """Class for the console program for the AirBnB project.

    Attributes:
        prompt (str): The command prompt string.
    """

    existing_classes = {"BaseModel": BaseModel}

    def __init__(self):
        """Initializes a new instance of the HBNBCommand class.

        Sets up the command prompt.
        """
        super().__init__()
        self.prompt = "(hbnb)$ "

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.

        Args:
            line (str): The command line arguments (class name).
        """
        if not line:
            print("** class name missing **")
        elif line in self.existing_classes.keys():
            obj = self.existing_classes[line]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id.

        Args:
            line (str): The command line arguments (separated by spaces).
        """
        """Print the str of an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.existing_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            key = args[0] + "." + args[1]
            working_obj = models.storage.all()
            if working_obj.get(key):
                print(working_obj[key])
            else:
                print("** no instance found **")
                    


    def do_destroy(self, line):
        """Destroys the item with the id specified in the json file"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.existing_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            key = args[0] + "." + args[1]
            working_obj = models.storage.all()
            if working_obj.get(key):
               del working_obj[key]
               models.storage.save()
            else:
                print("** no instance found **")
        

    def do_all(self, line):
        """Prints a string representation of all items with the specified class"""
        working_obj = models.storage.all()
        result = []
         
        if line:
            if line in self.existing_classes:
                for key, val in working_obj.items():
                    splitkey = key.split(".")
                    if splitkey[0] == line:
                        result.append(str(val))
            else:
                print("** class doesn't exist **")
        else:
            for v in working_obj.values():
                result.append(str(v))
        if result != []:
            print(result)            

    def do_update(self, line):
          """Updates an attribute of an object entry with the specified classname and id"""
          args = line.split()
          forbidden_atts = ['created_at', 'updated_at', 'id']
          if len(args) == 0:
              print("** class name missing **")
          elif(args[0] not in self.existing_classes):
              print("** class doesn't exist **")
          elif len(args) == 1:
               print("** instance id missing **")
          elif len(args) == 2 or args[2] in forbidden_atts:
               print("** attribute name missing **")
          elif len(args) == 3:
                print("** value missing **")
          else:
              working_objs = models.storage.all()
              key = "{}.{}".format(args[0], args[1])
              if key in working_objs:
                  value = working_objs.get(key)
                  try:
                      attr = getattr(value, args[2])
                      setattr(value, args[2], type(attr)(args[3]))
                  except AttributeError:
                      setattr(value, args[2], args[3])
                  models.storage.save()
              else:
                  print("** no instance found **")
    def do_quit(self, line):
        """Command to exit the program."""
        return True

    def do_EOF(self, line):
        """Command to exit the program."""
        return True

    def do_clear(self, line):
        """Clears the screen."""
        os.system("clear")

    def emptyline(self):
        """Handles empty line input."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
