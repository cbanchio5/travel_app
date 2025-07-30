from pydantic import BaseModel, Field
from typing import List
from datetime import date

class DayPlan(BaseModel):
    day: str
    activities: List[str]

class OptionPlan(BaseModel):
    name: str  # e.g., "option 1"
    days: List[DayPlan]

class ItineraryAlternative(BaseModel):
    title: str
    description: str
    location: str
    arrival: date
    departure: date
    itinerary: List[OptionPlan]

    model_config = {
        "json_schema_extra": {
            "required": [
                "title", "description", "location", "arrival", "departure", "itinerary"
            ]
        }
    }
