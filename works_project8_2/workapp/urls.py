from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert_data, name='insert'),
    path('query/', views.query_company, name='query'),
]
