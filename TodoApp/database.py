from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
Sqlite3
"""
# remember to change isactive -> is_active

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosApp.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread' : False})

"""
Postgres
"""

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Test123@localhost/TodoApplicationDatabase' #Postgres
# engine = create_engine(SQLALCHEMY_DATABASE_URL)


sessionLocal = sessionmaker(autoflush=False, autocommit = False, bind=engine)

Base = declarative_base()
