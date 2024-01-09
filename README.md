# Restaurants-SQLAlchemy-Code-Challenge


project details

This Python project implements a restaurant review system with a database backend using SQLAlchemy. It allows you to manage restaurants, customers, and reviews, as well as perform various operations related to them.

Technologies Used

 Python Alembic sqlalchemy

  Features

- **Restaurant Table:** Defines the structure for storing restaurant details such as name, location, and contact information.
- **Customer Table:** Represents the menus available at each restaurant, containing information like menu name and the restaurant it belongs to.
- **review Table:** Contains the items available in each menu, including details such as item name, description, and price.

 `models.py`: Entry point for creating database tables using SQLAlchemy. Contains the SQLAlchemy models defining the database schema for restaurants, menus, and items.
- `seed.py`: Seed file containing sample data to populate the database tables.
Usage of the project

    Restaurant Information: Easily access and manage restaurant details.

    Customer Records: Keep customer records up to date.

    Review System: Enable customers to leave detailed reviews for restaurants.

    Anagram Checker: Use the built-in anagram checker to find anagrams within a list of words.

Database Schema

The Restaurants Application uses a simple and effective database schema consisting of three tables:

    restaurants: Stores essential restaurant information, including names and price ranges.

    customers: Maintains customer records, including first names and last names.

    reviews: Records customer reviews for restaurants, including star ratings and feedback.

Here's a simplified schema diagram:

+---------------+        +--------------+        +-------------+
|  restaurants  |   1    |   reviews    |   N    |   customers |
|---------------| ------ |--------------| ------ |-------------|
| id            |        | id           |        | id          |
| name          |   <----| restaurant_id| ---->  | first_name  |
| price         |        | customer_id  |        | last_name   |
+---------------+        | star_rating
                            comments  |        +-------------+
                        | |
                        +--------------+


 ## Contributing

Contributions to the Restaurants Application are encouraged and welcome! If you have any suggestions, bug reports, or feature requests. If you'd like to contribute to the project, please fork the repository, make your changes, and submit a pull request.

### License

This project is licensed under the `MIT` License. 

## Author
It is written by Abdiqani adan 

## Github: https://github.com/Abduljr0/Restaurants-SQLAlchemy-Code-Challenge





