#!/usr/bin/python3
"""
author: Alfred Ternor

Model class for City
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    city class for table cities
    declarative_base
    Attributes:
        Base (class)
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False)
