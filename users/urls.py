from django.urls import path
from users import views as users_views

urlpatterns = [
    path('logout/', users_views.logout,name='logout'),
    path('', users_views.profile,name='profile'),
]