#!/usr/bin/python3
'''prints all City objects from the database hbtn_0e_14_usa'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    
    session = Session(engine)
    rows = session.query(State, City).join(City).all()

    for i in rows:
        print("{}: ({}) {}".format(i[0].__dict__['name'],
                                   i[1].__dict__['id'],
                                   i[1].__dict__['name']))

    session.close()
