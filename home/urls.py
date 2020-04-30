from django.urls import path
from home import views as home_views
from .views import PostsDetailView

urlpatterns = [
    path('', home_views.blog,name='home'),
    path('about/', home_views.about,name='about'),
    path('blog/', home_views.blog,name='blog'),
    path('post/', home_views.create_post,name='post'),
    path('post-details/<int:pk>/',PostsDetailView.as_view(),name='post-details'),
    path('post-update/<int:pk>/',home_views.post_update,name='post-update'),
    path('user/<str:username>/', home_views.user_post,name='user-post'),
]