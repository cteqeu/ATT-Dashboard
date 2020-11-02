# entities\databaseSessionManager.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# This class will return a database SQLAlchemy session,
# classes which want to manipulate data can use it to manipulate the database.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SERVER = 'localhost'
DATABASE = 'myAllThingsTalk'
DATABASE_CONNECTION = f'postgresql://11800991:admin123@localhost:5432/{DATABASE}'
engine = create_engine(DATABASE_CONNECTION, echo=True)

# create a Session
Session = sessionmaker(bind=engine)

class SessionManager(object):
    def __init__(self):
        self.session = Session()