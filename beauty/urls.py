from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('appointment/', views.create_appointment, name='appointment'),

    path('profile/', views.profile, name='profile'),

    path('reviews/', views.reviews, name='reviews'),

    # ДЕТАЛЬНЫЕ СТРАНИЦЫ
    path(
        'service/<int:id>/',
        views.service_detail,
        name='service_detail'
    ),

    path(
        'master/<int:id>/',
        views.master_detail,
        name='master_detail'
    ),
    path('message/reply/<int:message_id>/', views.master_reply, name='master_reply'),
]