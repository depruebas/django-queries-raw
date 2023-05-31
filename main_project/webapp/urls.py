from django.urls import path
from .views import index, add, delete

urlpatterns = [
    path('', index, name="index"),
    path('add', add, name="add"),
    path('delete', delete, name="delete"),
]