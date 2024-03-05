import cmd
import sys
class HBNBCommand(cmd.Cmd):
      """Class for the console program for the AirBnB project
          Attributes:
               prompt(str): The command prompt string
      """
      def __init__(self):
            """Initializes a new instance of the HBNBCommand class
               Sets up the command prompt
            """
            cmd.Cmd.__init__(self)
            self.prompt = '(hbnb)$ '
      def do_quagmire(self, line):
            """
            Tests if the command line works 
            Usage: quagmire
            """
            print("Giggity giggity")
      def do_exit(self, line):
            """Command to exit the program"""
            sys/exit(130)
      def do_EOF(self, line):
            """Command to exit the program"""
            sys.exit(130)
if __name__ == '__main__':
      HBNBCommand().cmdloop()