#!/usr/bin/python3
"""Model for the BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Parent class of all the rest of serializable classes
    Attributes:
        id (str): unique primary key of the instance
        created_at (datetime): creation time
        updated_at (datetime): update time
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the BaseModel class
        Args:
            *args: all the unamed arguments
            **kwargs: all the keyword arguments
        """
        if kwargs is None or len(kwargs) == 0:
            from . import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            del kwargs['__class__']
            self.__dict__ = kwargs
            self.__dict__['created_at'] = \
                datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__['updated_at'] = \
                datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def save(self):
        """
        Saves the current instance
        and updates the ``updated_at`` attributes to the current time
        """
        from . import storage
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Deserializes the current instance into a dictionary
        Returns:
            a dictionary representing all the instance attributes
        """
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return dict

    def __str__(self):
        """
        Returns the string representation of BaseModel.
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
