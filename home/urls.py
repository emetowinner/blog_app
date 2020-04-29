from django.urls import path
from home import views as home_views

urlpatterns = [
    path('', home_views.blog,name='home'),
    path('about/', home_views.about,name='about'),
    path('blog/', home_views.blog,name='blog'),
    path('post/', home_views.create_post,name='post'),
    path('user/<str:username>/', home_views.user_post,name='user-post'),
]