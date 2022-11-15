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


def generated_file():
    path = rf'C:\Users\Artem\projects\test_demoqa_webform\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path