from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import (
    Appointment,
    Review,
    MasterMessage
)


# РЕГИСТРАЦИЯ
class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:

        model = User

        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )


# ЗАПИСЬ
class AppointmentForm(forms.ModelForm):

    class Meta:

        model = Appointment

        fields = [
            'master',
            'service',
            'date',
            'time'
        ]


# ОТЗЫВ
class ReviewForm(forms.ModelForm):

    class Meta:

        model = Review

        fields = [
            'text',
            'rating'
        ]


# СООБЩЕНИЕ МАСТЕРУ
class MasterMessageForm(forms.ModelForm):

    class Meta:

        model = MasterMessage

        fields = ['message']

        widgets = {
            'message': forms.Textarea(
                attrs={
                    'rows': 4
                }
            )
        }