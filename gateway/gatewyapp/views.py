from django.http import JsonResponse, HttpResponse
from django.views import View
from django.conf import settings
import requests



class GateWayView(View):
    def get(self, request, path):
        try:
            response = requests.get(f"{settings.CORE_SERVER_URL}{request.path}", params=request.GET)
            if response.headers.get("Content-Type") == "application/json":
                return JsonResponse(response.json(), status=response.status_code)
            else:
                return HttpResponse(response.text, status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({"error": str(e)}, status=500)
    