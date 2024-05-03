#!/usr/bin/python3
"""Start link class to table in database 
"""
from os import getenv
from sqlalchemy import (create_engine)
from models.base_model import Base


class DBStorage:
    """Database storage engine
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")), pool_pre_ping=True
            )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Get all objects of the given class
        """
        