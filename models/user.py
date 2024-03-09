from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a user that inherits from the BaseModel class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
