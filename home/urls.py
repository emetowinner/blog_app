from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='home'),
    path('about/', about,name='about'),
    path('blog/', blog,name='blog'),
    path('login/', login,name='login'),
    path('logout/', logout,name='logout'),
    path('profile/', profile,name='profile'),
]