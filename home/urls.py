from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='home'),
    path('about/', about,name='about'),
    path('blog/', blog,name='blog'),
    path('post/', create_post,name='post'),
    path('user/<str:username>/', user_post,name='user-post'),
]