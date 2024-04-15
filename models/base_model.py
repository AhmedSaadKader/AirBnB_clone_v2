#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = self._parse_value(
            'created_at', kwargs.get('created_at')
            )
        self.updated_at = self._parse_value(
            'updated_at', kwargs.get('updated_at')
            )
        for key, value in kwargs.items():
            if key not in ['id', 'created_at', 'updated_at']:
                if key != '__class__':
                    setattr(self, key, value)
        # if not kwargs:
        storage.new(self)

    def _parse_value(self, method, value):
        """parse the values of the kwargs dictionary of init
        """
        if not value:
            value = datetime.now()
        elif isinstance(value, str):
            value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        elif not isinstance(value, datetime):
            raise ValueError(f"{method} must be a datetime object")
        return value

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
