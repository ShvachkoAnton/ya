from django.urls import path
from .views import PostList,New
urlpatterns=[
path('',PostList.as_view(), name='index'),
path('new/',New.as_view(), name='new')


]