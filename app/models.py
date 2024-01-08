from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///restaurants.db") 
Base.metadata.create_all(engine) 

Session = sessionmaker(bind=engine)
session = Session() 

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer())

    def __repr__(self):
        return f"Restaurant(id={self.id}, name={self.name}, price={self.price})"


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())


    def __repr__(self):
        return f'Customer(id={self.id}, first_name={self.first_name}, last_name={self.last_name})'


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))


    def __repr__(self):
        return f'Review(id={self.id}, comments={self.comments}, star_rating={self.star_rating})'
