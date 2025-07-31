from rest_framework.views import APIView
from rest_framework.response import Response
from celery.result import AsyncResult
from rest_framework import status
from apps.itinerary.services.itinerary_generator import generate_itinerary_options 
from apps.itinerary.services.client import OpenAIClientWrapper
from apps.itinerary.services.generator import ItineraryGenerator
from .tasks import generate_itinerary_task


class TestItineraryGeneratorView(APIView):
    def post(self, request):
        destination = request.data.get('destination')
        arrival = request.data.get('arrival')
        departure = request.data.get('departure')


        if not destination or not arrival or not departure:
            return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Launch the Celery task asynchronously
            task = generate_itinerary_task.delay(destination, arrival, departure)
            return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class ItineraryTaskStatusView(APIView):
    def get(self, request, task_id):
        task_result = AsyncResult(str(task_id))
        if task_result.state == 'PENDING':
            return Response({"status": "Pending"}, status=status.HTTP_202_ACCEPTED)
        elif task_result.state == 'SUCCESS':
            return Response({"status": "Success", "result": task_result.result}, status=status.HTTP_200_OK)
        elif task_result.state == 'FAILURE':
            return Response({"status": "Failure", "error": str(task_result.result)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"status": task_result.state}, status=status.HTTP_200_OK)