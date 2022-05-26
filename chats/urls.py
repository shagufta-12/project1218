
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as chat_views

urlpatterns = [
    path('', chat_views.home, name='chat-home'),
    path('login/', auth_views.LoginView.as_view(template_name="chat/login.html"), name='chat-login'),
    path('register/', chat_views.register, name='chat-register'),
    path('profile/', chat_views.profile, name='chat-profile'),
    path('send/', chat_views.send_chat, name='chat-send'),
    path('renew/', chat_views.get_messages, name='chat-renew'),
]
