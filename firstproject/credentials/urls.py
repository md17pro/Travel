from . import views
from django.urls import path

urlpatterns = [
    path('register',views.reg,name='Register'),
    path('login', views.log, name='login'),
    path('logout', views.logout, name='logout'),


]
