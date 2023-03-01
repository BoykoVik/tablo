from django.urls import path
from . import views

app_name = 'tablo'

urlpatterns = [
    path('', views.index, name='main'),
]
