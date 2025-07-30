import os
import json
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_itinerary_options(prompt_text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful travel assistant. Create 3 alternative itineraries for the destination."},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.7,
        max_tokens=800,
    )
    content = response['choices'][0]['message']['content']

    # Assuming response is JSON string:
    options_data = json.loads(content)
    return options_data['options']  # list of dicts with description & location