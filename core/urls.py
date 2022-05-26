
from django.urls import path
from core import views
from .views import *
from .form import MyChangePasswordForm , PasswordResetForm
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView

from chats import views as chats_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='/login/'), name='logout'),
    path('change-password/', PasswordChangeView.as_view(template_name="core/change-password.html", form_class=MyChangePasswordForm), name='change-password'),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name="core/password-change-done.html"), name="password_change_done"),
    path('reset-password/', PasswordResetView.as_view(template_name='core/reset-password.html', form_class= PasswordResetForm), name='reset-password'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
   

    path('chathome/', chats_views.home, name='chat-home'),
    path('login/', auth_views.LoginView.as_view(template_name="chat/login.html"), name='chat-login'),
    path('register/', chats_views.register, name='chat-register'),
    path('profile/', chats_views.profile, name='chat-profile'),
    path('send/', chats_views.send_chat, name='chat-send'),
    path('renew/', chats_views.get_messages, name='chat-renew'),


  

   
]

