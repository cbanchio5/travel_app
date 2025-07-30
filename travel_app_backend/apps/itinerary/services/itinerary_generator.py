import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
from datetime import date


print(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
env_path = os.path.join(os.path.dirname(__file__), '../../../travel_app_backend/.env')
load_dotenv(os.path.abspath(env_path))



class ItineraryAlternative(BaseModel):
    title: str
    description: str
    location: str
    arrival: date
    departure: date
    activities: List[str] = []


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_itinerary_options(destination, arrival, departure):
    prompt_text = f"destination: {destination}, arrival: {arrival}, departure: {departure}"
    
    response = client.responses.parse(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": "You are a helpful travel assistant. Create 3 alternative itineraries for the destination."},
        {
            "role": "user",
            "content": prompt_text,
        },
    ],
        text_format=ItineraryAlternative,
    )

    print(response)

    # Assuming response is JSON string:
    
    return "options_data"  # list of dicts with description & location
