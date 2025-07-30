from pydantic import BaseModel
from typing import Dict, List
from datetime import date

class ItineraryAlternative(BaseModel):
    title: str
    description: str
    location: str
    arrival: date
    departure: date
    itinerary: Dict[str, Dict[str, List[str]]] 
    class Config:
        json_schema_extra = {
            "required": [
                "title",
                "description",
                "location",
                "arrival",
                "departure",
                "itinerary",
            ]
        }

 