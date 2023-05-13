from django.urls import path
from . import views


app_name = 'food_to_recipe'
urlpatterns = [
    path('', views.index, name='index'),
]
