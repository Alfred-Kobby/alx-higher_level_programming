#!/usr/bin/python3
"""
author: Alfred Ternor
"""
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, data))
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State.name, City.id, City.name)\
                     .join(City, City.state_id == State.id)\
                     .order_by(City.id)
    for result in results:
        print("{}: ({}) {}".format(result[0], result[1], result[2]))
