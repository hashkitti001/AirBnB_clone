from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a user that inherits from the BaseModel class"""
    def __init__(self):
        """Initializes a new instance of the User class"""
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""


    