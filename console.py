#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
import re
import json

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '
    
    def do_quit(self, args):
        return True
    
    def help_quit(self):
        print ('Quit command to exit the program')
    
    def do_EOF(self, args):
        return True

    def help_EOF(self):
        print ('End of File')

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.

        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_create(self, arg):
        if(bool(arg)):
            if(arg == "BaseModel"):
                print("--**** Creating a new Object ****--")
                my_model = BaseModel()
                my_model.save()
                print(my_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        print("creates a new BaseModel object")


    def do_show(self, line):
        try:
            arg1,arg2 = [st for st in line.split()]
        except ValueError as ve:
            arg1 = line
            arg2 = ""

        if(bool(arg1)):
            if(arg1 == "BaseModel"):
                if (bool(arg2)):
                    check = 0
                    instance = ""
                    all_objs = storage.all()
                    for obj_id in all_objs.keys():
                        obj = str(obj_id).split(".")[1]
                        if arg2 == obj:
                            check = 1
                            instance = all_objs[obj_id]
                    if(check == 1):
                        print(instance)
                    else:
                        print("** instance id missing **")
                            
                else:
                    print("** no instance found **")
            else:
                print("**class doesn't exist **")
        else:
            print("** class name missing **")

    def help_show(slef):
        print("displays an instance of the BaseModel class if it exists")

    def do_destroy(self, line):
        try:
            arg1,arg2 = [st for st in line.split()]
        except ValueError as ve:
            arg1 = line
            arg2 = ""

        if(bool(arg1)):
            if(arg1 == "BaseModel"):
                if (bool(arg2)):
                    check = 0
                    instanceId = ""
                    all_objs = storage.all()
                    for obj_id in all_objs.keys():
                        obj = str(obj_id).split(".")[1]
                        if arg2 == obj:
                            check = 1
                            instanceId = obj_id
                        
                    if(check == 1):
                        all_objs.pop(instanceId)
                        storage.__objects = all_objs
                        storage.save()
                    else:
                        print("** instance id missing **")
                else:
                    print("** no instance found **")
            else:
                print("**class doesn't exist **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        print("deletes an instance form json file")

    def do_all(self, arg):
        if(bool(arg)):
            if(arg != "BaseModel"):
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                for obj_id in all_objs.keys():
                    print(all_objs[obj_id])
        else:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                print(all_objs[obj_id])
                
    def help_all(self):
        print("** prints all saved instances of BaseModel**")

    def do_update(self, line):
        try:
            arg1,arg2,key,value = [st for st in line.split()]
        except ValueError as ve:
            arg1 = line
            arg2 = ""

        if(bool(arg1)):
            if(arg1 == "BaseModel"):
                if (bool(arg2)):
                    check = 0
                    instance = ""
                    instanceKey = ""
                    all_objs = storage.all()
                    for obj_id in all_objs.keys():
                        obj = str(obj_id).split(".")[1]
                        if arg2 == obj:
                            check = 1
                            instance = all_objs[obj_id]
                            instanceKey = obj_id
                    if(check == 1):
                        if(bool(key)):
                            all_keys = json.load(re.findall(r"^{\b$}", instance))
                            instance.replace(re.findall(r"^{\b$}", instance), "")
                            for k in all_keys.keys():
                                if(key == k):
                                    all_keys[k] = value
                                    instance = instance + all_keys
                                    all_objs[instanceKey] = instance
                                    storage.__objects = all_objs
                                    storage.save()
                                else:
                                    print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** instance id missing **")
                            
                else:
                    print("** no instance found **")
            else:
                print("**class doesn't exist **")
        else:
            print("** class name missing **")

    def help_update(self):
        print("** updates the instances **"

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
