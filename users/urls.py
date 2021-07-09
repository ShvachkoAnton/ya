from django.urls import path
from .views import SignUpp,get_name
from . import views
urlpatterns=[
path('signup/',SignUpp.as_view(), name="signup")
,path('ok/', views.get_name, name='ok')


]