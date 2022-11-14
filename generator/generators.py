import random

from data.data import Person
from faker import Faker

faker_us = Faker('en_US')
Faker.seed()

value_subjects = ["Hindi", "English", "Maths", "Physics",
                  "Chemistry", "Biology", "Computer Science",
                  "Commerce", "Accounting", "Economics", "Arts",
                  "Social Studies", "History", "Civics"]

value_state = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]


def generator_person():
    yield Person(
        firstname=faker_us.first_name(),
        lastname=faker_us.last_name(),
        email=faker_us.email(),
        mobile=faker_us.msisdn(),
        current_address=faker_us.address(),
    )