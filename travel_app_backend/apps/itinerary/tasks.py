import os
from celery import shared_task
from datetime import date
from apps.itinerary.services.generator import ItineraryGenerator
from apps.itinerary.services.client import OpenAIClientWrapper
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '../../travel_app_backend/.env')
load_dotenv(os.path.abspath(env_path))



client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@shared_task
def generate_itinerary_task(destination, arrival_str, departure_str):
    arrival = date.fromisoformat(arrival_str)
    departure = date.fromisoformat(departure_str)

    client = OpenAIClientWrapper(client=client)  # Inject your real client here
    generator = ItineraryGenerator(client=client)
    itinerary = generator.generate(destination, arrival, departure)

    # You might want to save to DB here instead of returning
    return itinerary.dict()
