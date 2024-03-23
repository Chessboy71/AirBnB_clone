#!/usr/bin/python3

""" This file is for the baseModel for the airbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ this is the contructor of the baseModel class
        """
        self.id = uuid.uuid4().__str__()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ this is the method to save the class
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ this is the first function for the serialization
        """
        mydict = {}
        for key, value in self.__dict__.items():
            if type(value) == datetime:
                mydict[key] = value.isoformat()
            else:
                mydict[key] = value
        mydict["__class__"] = self.__class__.__name__
        return mydict

    def __str__(self):
        """
        str funtion 
        """
        csname = self.__class__.__name__
        return "[{}] ({}) {}".format(csname, self.id, self.__dict__)
