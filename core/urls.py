
from django.urls import path
from .views import *
from .form import MyChangePasswordForm , PasswordResetForm
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView
from chat import views as chat_views
from private_chat import views as private_chat_views

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
    path('home', chat_views.home, name='home'),
    path('<str:room>/', chat_views.room, name='room'),
    path('checkview', chat_views.checkview, name='checkview'),
    path('send', chat_views.send, name='send'),
    path('getMessages/<str:room>/', chat_views.getMessages, name='getMessages'),

    path('index/', private_chat_views.index, name='index'),
    path('<str:username>', private_chat_views.private_chatPage, name='chat'),

   
]



