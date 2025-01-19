from django.http import JsonResponse, HttpResponse
from django.views import View
import requests

CORE_SERVER_URL = 'http://127.0.0.1:8000/'

class GateWayView(View):
    def get(self, request, path):
        try:
            response = requests.get(f"{CORE_SERVER_URL}{request.path}", params=request.GET)
            if response.headers.get("Content-Type") == "application/json":
                return JsonResponse(response.json(), status=response.status_code)
            else:
                return HttpResponse(response.text, status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({"error": str(e)}, status=500)
    