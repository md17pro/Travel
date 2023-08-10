from . import views
from django.urls import path
app_name='demo'
urlpatterns = [
    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='result'),
    # path('contacts/',views.contacts,name='contacts')
]
