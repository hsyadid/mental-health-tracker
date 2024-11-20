from django.urls import path
from authentication.views import login, register, create_mood_flutter, logout

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('create-flutter/', create_mood_flutter, name='create_mood_flutter'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]