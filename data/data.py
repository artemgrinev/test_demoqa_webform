from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    firstname: str = None
    lastname: str = None
    mobile: str = None