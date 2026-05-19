from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('beauty.urls')),

    # ВХОД
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='beauty/login.html'
        ),
        name='login'
    ),

    # ВЫХОД
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # СМЕНА ПАРОЛЯ
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='beauty/password_change.html'
        ),
        name='password_change'
    ),

    path(
        'password_change_done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='beauty/password_change_done.html'
        ),
        name='password_change_done'
    ),
]