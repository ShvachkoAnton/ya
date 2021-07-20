from posts.models import Profile
from django.urls import path
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from .views import News,PostList,user_posts,post_view,Update,comment_add,user_list,user_detail,user_follow,followToggle,profile
from django.test import SimpleTestCase, override_settings
from django.shortcuts import render


urlpatterns=[path('',PostList.as_view(), name='index'),
path('users/',user_list,name='user_list'),
path('users/follow/',user_follow, name='user_follow'),
path("profile/<str:username>/", profile, name="profilee"),
path("followToggle/<str:author>/",followToggle, name="followToggle"),

path('users/<str:username>/',user_detail,name='user_detail'),

path('<str:username>/new/',News.as_view(), name='new'),
path('<str:username>/', user_posts, name='profile'),
path('<str:username>/<int:post_id>/', post_view, name='tak'),
path('<str:username>/<int:post_id>/add_comment/', comment_add, name='add_comment'),

path('<str:username>/<int:post_id>/edit/', Update.as_view(), name='edit'),






]

