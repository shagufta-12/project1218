from django.urls import path
from . import views
from private_chat.views import index, private_chatPage

urlpatterns = [
path('', index, name='index'),
path('<str:username>', private_chatPage, name='chat'),
]
