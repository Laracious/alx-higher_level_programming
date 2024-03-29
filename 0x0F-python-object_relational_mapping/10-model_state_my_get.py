#!/usr/bin/python3
"""
    Get the states of database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        result = session.query(State).filter_by(name=sys.argv[4]).first()
        print("{}".format(result.id))
    except:
        print("Not found")

