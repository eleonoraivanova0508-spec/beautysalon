from .models import Notification

def notification_count(request):
    """Контекст-процессор для количества непрочитанных уведомлений"""
    if request.user.is_authenticated:
        count = request.user.notifications.filter(is_read=False).count()
        return {'notification_count': count}
    return {'notification_count': 0}