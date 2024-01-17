from django.urls import path

from .views import BotList, BotDetails, Register, Login

urlpatterns = [
    path('bots/', BotList.as_view(), name='bot_list'),
    path('bots/<int:id>/', BotDetails.as_view(), name='bot_details'),
    path('users/', Register.as_view(), name='register'),
    path('users/login/', Login.as_view(), name='login'),
]
