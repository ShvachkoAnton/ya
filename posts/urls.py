from posts.models import Profile
from django.urls import path
from .views import News,PostList,user_posts,post_view,Update
urlpatterns=[
path('',PostList.as_view(), name='index'),
path('<str:username>/new/',News.as_view(), name='new'),
path('<str:username>/', user_posts, name='profile'),
path('<str:username>/<int:post_id>/', post_view, name='tak'),
path('<str:username>/<int:post_id>/edit/', Update.as_view(), name='edit'),
        # Просмотр записи

        

]