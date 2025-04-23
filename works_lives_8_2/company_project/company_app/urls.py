from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert_works, name='insert_works'),
    path('search/', views.retrieve_people, name='retrieve_people'),
    path('', views.index, name='home_page')
]
