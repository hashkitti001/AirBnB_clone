import cmd
import os
import sys

from models.base_model import BaseModel
import models


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
        pass

    def do_update(self, line):
        pass

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

