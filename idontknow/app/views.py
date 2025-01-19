from django.http import JsonResponse
import requests

def send(request): 
    return JsonResponse({"message" : "English or Spanish?"})
    
