#!/usr/bin/python3
"""
Write a Python file similar to model_state.py
named model_city.py that contains the class definition of a City
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State, City).join(City).all()

    for i in rows:
        print("{}: ({}) {}"
        .format(i[0].__dict__['name'], i[1].__dict__['id'],
        i[1].__dict__['name']))

    session.close()
