#!/usr/bin/python3
'''prints the State object with the name passed
 as argument from the database hbtn_0e_6_usa'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    rows = session.query(State).all()

    res = ""

    for i in rows:
        if sys.argv[4] in i.__dict__['name']:
            res = i.__dict__['id']

    if res != "":
        print(res)
    else:
        print("Not found")

    session.close()
