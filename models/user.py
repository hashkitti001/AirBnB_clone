from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
class User(BaseModel):
    """Class representing a user with specific attributes"""
    def __init__(self):
        """Initializes a new instance of the User class"""
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""


    