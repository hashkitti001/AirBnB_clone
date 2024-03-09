from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing an review that inherits from the BaseModel class"""
    place_id = ""
    user_id = ""
    text = ""
