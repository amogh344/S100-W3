# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<str:day>/', views.task_view, name='task_view'),
]