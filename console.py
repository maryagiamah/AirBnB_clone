#!/usr/bin/python3
"""Entry point of the command interpreter """


import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command line interpreter """

    prompt = '(hbnb) '
    all_models = ["BaseModel", "User", "City", "Place", 
                  "State", "Amenity", "Review"]

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing for empty line"""
        pass

    def do_create(self, cls_name):
        """Creates a new instance of BaseModel, save it to json file """
        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in self.all_models:
            print("** class doesn't exist **")
            return
        new_instance = eval(cls_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.all_models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            obj = models.storage.all()[f"{args[0]}.{args[1]}"]
            print(obj)
        except KeyError:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.all_models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            obj = models.storage.all()
            del obj[f"{args[0]}.{args[1]}"]
        except KeyError:
            print("** no instance found **")
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances """
        if arg and arg not in self.all_models:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in models.storage.all().values()])

    def do_update(self, arg):
        """Updates an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.all_models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            obj = models.storage.all()[f"{args[0]}.{args[1]}"]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(obj, args[2], args[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
