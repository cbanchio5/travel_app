from datetime import date
import logging
from pydantic import ValidationError
from openai import OpenAIError

from apps.itinerary.services.prompt_builder import PromptBuilder
from apps.itinerary.services.client import OpenAIClientWrapper
from apps.itinerary.services.validators import DateValidator
from apps.itinerary.models.itinerary_schema import ItineraryAlternative

logger = logging.getLogger(__name__)

class ItineraryGenerator:
    def __init__(
        self,
        client: OpenAIClientWrapper,
        model: str = "gpt-4o-mini"
    ):
        self.client = client
        self.model = model

    def generate(self, destination: str, arrival: date, departure: date) -> ItineraryAlternative:
        try:
            # 1. Validate inputs
            DateValidator.validate_arrival_departure(arrival, departure)

            # 2. Build prompt
            prompt_builder = PromptBuilder(destination, arrival, departure)
            user_prompt = prompt_builder.build_user_prompt()
            system_prompt = prompt_builder.build_system_prompt()

            # 3. Call OpenAI
            response = self.client.get_structured_response(
                system=system_prompt,
                user=user_prompt,
                model=self.model,
                text_format=ItineraryAlternative
            )

            logger.info(f"Successfully generated itinerary for {destination}")
            return response

        except (OpenAIError, ValidationError, Exception) as e:
            logger.exception(f"Failed to generate itinerary: {e}")
            raise RuntimeError(f"Itinerary generation failed: {e}")
