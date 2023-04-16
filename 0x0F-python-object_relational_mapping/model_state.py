#!/usr/bin/python3
"""
author: Alfred Ternor

Model class for State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    state class for table state
    declarative_base
    Attributes:
        Base (class)
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
