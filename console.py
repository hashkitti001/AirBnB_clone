import cmd
import sys
import os
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """Class for the console program for the AirBnB project.

    Attributes:
        prompt (str): The command prompt string.
    """
    all_classes = {
        "BaseModel": BaseModel
    }
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
        bm_instance = BaseModel()
        bm_instance.__class__.__name__ = line

        if not line:
            print("** class name missing **")
        elif self.all_classes.get(line):
            obj = self.all_classes[line]
        else:
            bm_instance.save()
            print(bm_instance.id)

    def do_show(self, line):
        pass

    def do_destroy(self, line):
        pass

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
