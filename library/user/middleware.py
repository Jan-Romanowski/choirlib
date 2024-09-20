from django.utils import timezone
from datetime import timedelta

class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            now = timezone.now()
            # Обновляем поле раз в 5 минут
            if request.user.last_activity is None or now - request.user.last_activity > timedelta(minutes=5):
                request.user.last_activity = now
                request.user.save(update_fields=['last_activity'])

        return response
