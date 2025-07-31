import os
from celery import shared_task
from datetime import date
from apps.itinerary.services.generator import ItineraryGenerator
from apps.itinerary.services.client import OpenAIClientWrapper
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)


env_path = os.path.join(os.path.dirname(__file__), '../../travel_app_backend/.env')
load_dotenv(os.path.abspath(env_path))



real_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@shared_task
def generate_itinerary_task(destination, arrival_str, departure_str):
    arrival = date.fromisoformat(arrival_str)
    departure = date.fromisoformat(departure_str)
    logger.info(f"Real client: {real_client}")

    openai_client = OpenAIClientWrapper(client=real_client)  
    generator = ItineraryGenerator(client=openai_client)
    itinerary = generator.generate(destination, arrival, departure)

   
    return itinerary.dict()
