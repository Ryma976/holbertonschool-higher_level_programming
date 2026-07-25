#!/usr/bin/python3
"""Contains the State model with relationship to City."""
from relationship_city import Base, City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(Base):
    """State class linking to the states table."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City',
        backref='state',
        cascade='all, delete, delete-orphan',
        order_by='City.id'
    )
