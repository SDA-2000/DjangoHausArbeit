from django.http import JsonResponse, HttpResponse
import requests

CORE_SERVER_URL = 'http://127.0.0.1:8000/'

def watch(requrest):
    try:
        response = requests.get(CORE_SERVER_URL)
        return JsonResponse(response.json(), status=response.status_code)
    except requests.RequestException:
        return JsonResponse({"error": "Failed to connect to the first server", "details": str(requests.RequestException)}, status=500)
        