from django.http import JsonResponse, HttpResponse
import requests

core_endp = 'http://0.0.0.0:9283/'

def watch(requrest):
    try:
        response = requests.get(core_endp)
        return JsonResponse(response.json(), status=response.status_code)
    except requests.RequestException:
        return("Cant connect to core server!")
        