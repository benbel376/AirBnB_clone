#!/usr/bin/python3
"""file containing basemodel class"""
import uuid
import datetime
from models import storage


class BaseModel:
	"""Class BaseModel, base model for AirBnB Clone"""
	
    def __init__(self, *args, **kwargs):
	"""initializes BaseModel"""
        if(bool(kwargs)):
            for key in kwargs.keys():
                if(key != '__class__'):
                    setattr(self, key, kwargs[key])
                    self.created_at = datetime.datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f') 
                    self.updated_at = datetime.datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
			
    def __str__(self):
	"""class str method"""
        return '[{}] ({}) {}'.format(type(self).__name__, self.id, self.__dict__)    
   
    def save(self):
	"""updates updated_at with current time"""
        self.updated_at = datetime.datetime.now()
        storage.save()
		
    def to_dict(self):
	"""creates a dictionary of BaseModel"""
        selu = self.__dict__
        selu['__class__'] = type(self).__name__
        selu['updated_at'] = self.updated_at.isoformat();
        selu['created_at'] = self.created_at.isoformat();
        return self.__dict__
