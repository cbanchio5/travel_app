import os
import json
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
from apps.itinerary.models.itinerary_schema import ItineraryAlternative

env_path = os.path.join(os.path.dirname(__file__), '../../../travel_app_backend/.env')
load_dotenv(os.path.abspath(env_path))



client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_itinerary_options(destination, arrival, departure):
    prompt_text = f"destination: {destination}, arrival: {arrival}, departure: {departure}"
    
    try:
        response = client.responses.parse(
         model="gpt-4o-mini",
            input=[
            {"role": "system", "content": "You are a helpful travel assistant. Create 3 alternative itineraries for the destination. They should all include what to do and see on each day. Structure should be a dictionary of alternatives, each alternative being a dictionary of their own containing what to do on each day"},
            {
            "role": "user",
            "content": prompt_text,
            },
            ],
            text_format=ItineraryAlternative,
            )
    except OpenAIError as e:
        raise RuntimeError(f"OpenAI API error: {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {e}")

    print(response.output[0].content[0].parsed)
    print(type(response))

    # Assuming response is JSON string:
    
    return response.output[0].content[0].parsed  # list of dicts with description & location
