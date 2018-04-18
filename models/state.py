#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")

        @property
        def cities(self):
            matching_cities = []
            for city in self.cities:
                if city.state_id == self.id:
                    matching_cities.append(city)

            return (matching_cities)
    else:
        name = ""

        @property
        def cities(self):
            city_list = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return (city_list)

#Ref: https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete
