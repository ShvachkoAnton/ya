from django.urls import path
from .views import New,PostList,profile
urlpatterns=[
path('',PostList.as_view(), name='index'),
path('new/',New.as_view(), name='new'),
path('<int:pk>/profile/', profile, name='profile'),
        # Просмотр записи

        

]