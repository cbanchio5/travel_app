from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.itinerary.services.itinerary_generator import generate_itinerary_options  # adjust import path

@api_view(['POST'])
def test_itinerary_generator(request):
    # Expecting JSON input with destination, arrival, departure:
    destination = request.data.get('destination')
    arrival = request.data.get('arrival')
    departure = request.data.get('departure')

    if not all([destination, arrival, departure]):
        return Response({"error": "Please provide destination, arrival, and departure."},
                        status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Call your itinerary generator service
        itineraries = generate_itinerary_options(destination, arrival, departure)
        
        # Return the generated itineraries directly in the response
        return Response(itineraries, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
