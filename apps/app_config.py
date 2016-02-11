
__author__ = "Ashwini Chandrasekar(@sriniash)"
__email__ = "ASHWINI_CHANDRASEKAR@homedepot.com"
__version__ = "1.0"
__doc__ = "Application db config"


import os

from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.pool import NullPool

file_path = os.path.abspath(os.getcwd()) + "/apps/data/devtools.db"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path
SQLALCHEMY_RECORD_QUERIES = True


'''
  SQL DB


# SQLALCHEMY_DATABASE_URI = 'mysql://username:password@ip-address/db_name'

'''

engine = create_engine(SQLALCHEMY_DATABASE_URI, poolclass=NullPool)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

