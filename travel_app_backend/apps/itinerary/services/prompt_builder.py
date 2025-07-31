from datetime import date
from apps.itinerary.services.prompt import ITINERARY_GENERATION_SYSTEM_PROMPT

class PromptBuilder:
    def __init__(self, destination: str, arrival: date, departure: date):
        self.destination = destination
        self.arrival = arrival
        self.departure = departure

    def build_user_prompt(self) -> str:
        days = (self.departure - self.arrival).days
        return (
            f"destination: {self.destination}, "
            f"arrival: {self.arrival}, "
            f"departure: {self.departure}, "
            f"duration: {days} days"
        )

    def build_system_prompt(self) -> str:
        return ITINERARY_GENERATION_SYSTEM_PROMPT
