from django.http import JsonResponse, HttpResponse
import requests

CORE_SERVER_URL = 'http://0.0.0.0:9283'

def watch(requrest):
    try:
        response = requests.get(CORE_SERVER_URL)
        return JsonResponse(response.json(), status=response.status_code)
    except requests.RequestException as e:
        return JsonResponse({"error": "Failed to connect to the first server", "details": str(e)}, status=500)
        