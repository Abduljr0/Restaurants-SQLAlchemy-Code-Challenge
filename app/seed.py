from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Restaurant, Review, Customer, Base

