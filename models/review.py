from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing an review that inherits from the BaseModel class"""
    def __init__(self):
        """Initializes a new instance of the Review class"""
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""



    