from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_institute, name='select_institute'),
    path('details/<int:institute_id>/', views.institute_details, name='institute_details'),
]
