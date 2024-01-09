from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Restaurant, Review, Customer, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurant_reviews.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()

    fake = Faker()

    # Seed data for restaurants
    restaurants = []
    for i in range(50):
        restaurant = Restaurant(
            name=fake.company(),
            price=random.randint(100, 5000)
        )
        session.add(restaurant)
        restaurants.append(restaurant)
    session.commit()

    # Seed data for customers
    customers = []
    for i in range(300):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer)
        customers.append(customer)
    session.commit()

    # Seed data for reviews
    reviews = []
    for i in range(200):
        restaurant = random.choice(restaurants)
        customer = random.choice(customers)

        review = Review(
            comments=fake.sentence(),
            star_rating=random.randint(1, 10),
            customer_id=customer.id,
            restaurant_id=restaurant.id
        )

        session.add(review)
        reviews.append(review)
    session.commit()

    print("Total Restaurants are: ", session.query(Restaurant).count())  # 50 Restaurants
    print("Total customer:", session.query(Customer).count())  # 300 customers
    print("Total review:", session.query(Review).count())  # 200 reviews

    session.close()