from models.base_model import BaseModel


class State(BaseModel):
    """Class representing a state entity that inherits from the BaseModel class"""
    def __init__(self):
        """Initializes a new instance of the State class"""
        super().__init__()
        self.name = ""
