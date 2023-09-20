from dataclasses import dataclass

# MongoDB model for users
@dataclass
class User:
    _id: str
    email: str
    password: str
