from models import RequestHistory

class RequestHistoryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Обработка запроса перед тем, как передать его дальше
        response = self.get_response(request)

        # Сохранение информации о запросе
        RequestHistory.objects.create(
            ip_address=request.META.get('REMOTE_ADDR'),
            url=request.build_absolute_uri(),
            method=request.method,
            user_agent=request.META.get('HTTP_USER_AGENT', '')
        )

        return response