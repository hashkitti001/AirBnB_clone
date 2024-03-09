from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing an amenity that inherits from the BaseModel class"""
    def __init__(self):
        """Initializes a new instance of the Amenity class"""
        super().__init__()
        self.name = ""


    