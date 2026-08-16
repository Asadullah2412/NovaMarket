from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://postgres:asad123@localhost:5432/users' # change the address 

# creating engine 
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autoflush=False,bind=engine)

Base = declarative_base()
