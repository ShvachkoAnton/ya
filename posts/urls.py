from posts.models import Profile
from django.urls import path
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from .views import News,PostList,user_posts,post_view,Update
from django.test import SimpleTestCase, override_settings
from django.shortcuts import render


urlpatterns=[
path('',PostList.as_view(), name='index'),
path('<str:username>/new/',News.as_view(), name='new'),
path('<str:username>/', user_posts, name='profile'),
path('<str:username>/<int:post_id>/', post_view, name='tak'),
path('<str:username>/<int:post_id>/edit/', Update.as_view(), name='edit'),]

        # Просмотр записи


