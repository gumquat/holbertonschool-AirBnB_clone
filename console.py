#!/usr/bin/python3
""" console """
import cmd
from models.models import models_dict
from model.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ console """
    prompt = '(hbnb)'

    def do_hello(self, line):
        """Prints a greeting message"""
        print("Hello, world!")

    def do_quit(self, line):
        """Exits the shell ... EOF"""
        return True

    def do_EOF(self, line):
        """Exits the shell"""
        return True

    # Override emptyline() to avoid repeating the last command
    def emptyline(self):
        """empty line + 'enter' executes nothing"""
        pass

    # def help [this is autoincluded]

    def do_create(self, arg):
        """creates new inst of BaseModel saved to json file and prints ID"""
        if not arg:
            print("** class name missing **")
        elif arg not in models_dict.keys():
            print("** class doesn't exist **")
        else:
            new_model = models_dict[arg]()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """print string rep of instance"""
        args = arg.split()
        class_name = args[0]
        instance_id = args[1]
        obj_dict = models_dict.storage.all() # double check this!

        if not args:
            print("** class name missing **")
            return
        if class_name not in models_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = (f"{class_name}.{instance_id}")
        if key not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[key])

    # def destroy

    # all

    # update

if __name__ == '__main__':
    HBNBCommand().cmdloop()
