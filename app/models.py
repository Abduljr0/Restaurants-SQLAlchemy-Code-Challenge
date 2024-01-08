from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///restaurants.db") 
Base.metadata.create_all(engine) 