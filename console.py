#!/usr/bin/python3
"""Entry point of the command interpreter """


import cmd
import models
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command line interpreter """

    prompt = '(hbnb) '
    all_models = ["BaseModel", "User"]

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
        if cls_name:
            if cls_name not in all_models:
                print("** class doesn't exist **")
                return
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in all_models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        reg_no = args[1]

        try:
            obj = models.storage.all()[f"{cls_name}.{reg_no}"]
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

        cls_name = args[0]
        if cls_name not in all_models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        reg_no = args[1]
        try:
            obj = models.storage.all()
            del obj[f"{cls_name}.{reg_no}"]
        except KeyError:
            print("** no instance found **")
        models.storage.save()
    def do_all(self, arg):
        """Prints all string representation of all instances """
        if arg and arg not in all_models:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in models.storage.all().values()])

    def do_update(self, arg):
        """Updates an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]

        if cls_name not in all_models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        reg_no = args[1]

        try:
            obj = models.storage.all()[f"{cls_name}.{reg_no}"]
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
