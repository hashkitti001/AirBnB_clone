from models.base_model import BaseModel


class Place(BaseModel):
    """Class representing a place that inherits from the BaseModel class"""
    def __init__(self):
        """Initializes a new instance of the Place class"""
        super().__init__()
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_id = []


    