from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login,name='login'),
    path('logout/', logout,name='logout'),
    path('profile/', profile,name='profile'),
    path('', register,name='register'),
]