from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# УСЛУГИ
class Service(models.Model):

    title = models.CharField(max_length=100)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    duration = models.IntegerField()

    image = models.URLField(blank=True)

    def __str__(self):
        return self.title


# МАСТЕРА
class Master(models.Model):

    full_name = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    experience = models.IntegerField()

    avatar = models.URLField(blank=True)

    description = models.TextField(blank=True)
    user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    def __str__(self):
        return self.full_name


# РАБОТЫ МАСТЕРА
class MasterWork(models.Model):

    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        related_name='works'
    )

    image = models.URLField()

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# СООБЩЕНИЯ МАСТЕРУ
class MasterMessage(models.Model):

    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    message = models.TextField()

    # НОВОЕ: ответ мастера
    reply = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} -> {self.master.full_name}"

# ЗАПИСИ
class Appointment(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Ожидание'),
        ('approved', 'Подтверждено'),
        ('cancelled', 'Отменено'),
    )

    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f"{self.client.username} - {self.service.title}"


# ОТЗЫВЫ
class Review(models.Model):

    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    rating = models.IntegerField()

    def __str__(self):
        return f"Отзыв от {self.client.username}"