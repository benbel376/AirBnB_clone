#!/usr/bin/python3
"""File Storage for AirBnB Clone"""
import json
from os.path import exists


class FileStorage:
    """Class for FileStorage"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """inserts obj in __objects """
        self.__objects[type(obj).__name__ + "." + obj.id] = obj.__str__()

    def save(self):
        """serialize __objects to JSON file"""
        tmp = dict()
        for keys in self.__objects.keys():
            temp[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, mode='w') as json_file:
            json.dump(tmp, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from ..city import City
        from ..amenity import Amenity
		from ..place import Place
		from ..base_model import BaseModel
        from ..review import Review
		from ..user import User
        from ..state import State
        
        

        if exists(self.__file_path):
            with open(self.__file_path) as json_file:
                reloaded_dict = json.load(json_file)
            for keys in reloaded_dict.keys():
                if reloaded_dict[keys]['__class__'] == "BaseModel":
                    self.__objects[keys] = BaseModel(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "User":
                    self.__objects[keys] = User(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "State":
                    self.__objects[keys] = State(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "City":
                    self.__objects[keys] = City(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "Amenity":
                    self.__objects[keys] = Amenity(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "Place":
                    self.__objects[keys] = Place(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "Review":
                    self.__objects[keys] = Review(**reloaded_dict[keys])
