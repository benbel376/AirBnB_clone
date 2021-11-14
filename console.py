#!/usr/bin/python3
"""
A command line interpreter for AirBnB clone
"""

import cmd
from models.city import City
from models import storage
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.state import State



class HBNBCommand(cmd.Cmd):
    """
        the console class
    """

    prompt = '(hbnb) '
    __class_names = {
        BaseModel.__name__: BaseModel,
        User.__name__: User,
        State.__name__: State,
        City.__name__: City,
        Place.__name__: Place,
        Amenity.__name__: Amenity,
        Review.__name__: Review
    }
    __methods = ["all", "count", "show", "destroy", "update"]

    @staticmethod
    def extract(arg, id=" "):
        """
			converts string to arguments list
        """

        arguments = arg.split(id)
        narguments = []

        for x in arguments:
            if x != '':
                narguments.append(x)
        return narguments

    def do_quit(self, arg):
        """Exits the program"""

        return True

    def help_quit(self):
        """Prints help for the quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Exits the program"""

        print("")
        return True

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints
            the id.
                Ex: $ create BaseModel
        """

        arg_lst = HBNBCommand.extract(arg)
        if len(arg_lst) == 0:
            print("** class name missing **")
            return False

        if len(arg_lst) > 1:
            print("** to many arguments **")
            return False

        if (arg_lst[0] in HBNBCommand.__class_names.keys()):
            new_obj = HBNBCommand.__class_names[arg_lst[0]]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """
            prints Help info for the create function
        """
        print("** Creats a new instance of the specified class **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance
        """
        arg_lst = HBNBCommand.extract(arg)
        db = storage.all()
        if not len(arg_lst):
            print("** class name missing **")
        elif (arg_lst[0] not in HBNBCommand.__class_names.keys()):
            print("** class doesn't exist **")
        elif len(arg_lst) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_lst[0], arg_lst[1]) not in db:
            print("** no instance found **")
        else:
            print(db["{}.{}".format(arg_lst[0], arg_lst[1])])


    def help_show(self):
        """
            Prints Help for the show function
        """
        print("** prints the objects instance **")

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
        """
        arg_lst = HBNBCommand.extract(arg)
        storage.reload()
        db = storage.all()
        if not len(arg_lst):
            print("** class name missing **")
        elif (arg_lst[0] not in HBNBCommand.__class_names.keys()):
            print("** class doesn't exist **")
        elif len(arg_lst) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_lst[0], arg_lst[1]) not in db:
            print("** no instance found **")
        else:
            # print(storage.__class__.__name__.__objects)
            del db["{}.{}".format(arg_lst[0], arg_lst[1])]
            storage.save()

    def help_destroy(self):
        """
            Prints Help for the destroy function
        """
        print("** deletes an instance from JSON file **")

    def do_all(self, arg):
        """
            Prints all string representation of all instances
        """
        arguments = HBNBCommand.extract(arg)
        if len(arguments) > 0 and arguments[0] not in HBNBCommand.__class_names:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(arguments) > 0 and arguments[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(arguments) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def help_all(self):
        """
            prints help for the all function
        """
        print("** prints all string representation of all the instances **")

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
                Ex: $ update BaseModel 1234-1234-1234 email
                      "aibnb@holbertonschool.com"
        """
        arguments = HBNBCommand.extract(arg)
        objdict = storage.all()

        if len(arguments) == 0:
            print("** class name missing **")
            return False
        if arguments[0] not in HBNBCommand.__class_names:
            print("** class doesn't exist **")
            return False
        if len(arguments) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arguments[0], arguments[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arguments) == 2:
            print("** attribute name missing **")
            return False
        if len(arguments) == 3:
            try:
                type(eval(arguments[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arguments) == 4:
            obj = objdict["{}.{}".format(arguments[0], arguments[1])]
            if arguments[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arguments[2]])
                obj.__dict__[arguments[2]] = valtype(arguments[3])
            else:
                obj.__dict__[arguments[2]] = arguments[3]
        elif type(eval(arguments[2])) == dict:
            obj = objdict["{}.{}".format(arguments[0], arguments[1])]
            for k, v in eval(arguments[2]).items():
                if (k in obj.__class__.__dict__.keys() and type(
                        obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def help_update(self):
        """
            prints Help for the update function
        """
        print(
            """Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
                Ex: $ update BaseModel 1234-1234-1234
                      email "aibnb@holbertonschool.com""")

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.

        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_count(self, arg):
        """
            Prnits the number of elements inside the FileStorage that
            are of instances of cls
        """
        arguments = HBNBCommand.extract(arg)
        if len(arguments) > 0 and arguments[0] not in HBNBCommand.__class_names:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(arguments) > 0 and arguments[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(arguments) == 0:
                    objl.append(obj.__str__())
            print(len(objl))

    def show(self, cls):
        """
            Gives all the elements inside the FileStorage that
            are of instances of cls
        """
        pass

    def destroy(self, cls):
        """
            Gives all the elements inside the FileStorage that
            are of instances of cls
        """
        pass

    def update(self, cls):
        """
            Gives all the elements inside the FileStorage that
            are of instances of cls
        """
        pass

    def default(self, line):
        """
            Handles the case where the the command has no equivlaent
            do_ method
        """

        line_p = HBNBCommand.extract(line, '.')
        if line_p[0] in HBNBCommand.__class_names.keys() and len(line_p) > 1:
            if line_p[1][:-2] in HBNBCommand.__methods:
                func = line_p[1][:-2]
                cls = HBNBCommand.__class_names[line_p[0]]
                eval("self.do_" + func)(cls.__name__)
            else:
                print("** class doesn't exist **")
        else:
            super().default(line)
        return False


if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop()
