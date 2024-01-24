from django.urls import path
from .views import home, todo

urlpatterns = [
    path('home', home),
    path('todo', todo)
]