from django.http import JsonResponse, HttpResponse
import requests

CORE_SERVER_URL = 'http://0.0.0.0:9283'

def watch(requrest, subpath):
    core_endp = f"{CORE_SERVER_URL}/{subpath}"
    method = requests.method
    data = requests.body

    headers = {
        "Content-Type": request.headers.get("Content-Type", "application/json"),
    }

    try:
        # Перенаправляем запрос на Core-сервер
        response = requests.request(method, core_url, data=data, headers=headers)

        # Возвращаем ответ от Core-сервера клиенту
        return HttpResponse(response.content, status=response.status_code, content_type=response.headers['Content-Type'])
    except requests.exceptions.RequestException as e:
        # Обработка ошибок соединения с Core-сервером
        return JsonResponse({"error": "Не удалось подключиться к Core-серверу", "details": str(e)}, status=502)
        