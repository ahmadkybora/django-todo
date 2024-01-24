from django.shortcuts import render, HttpResponse
from .models import TodoModel

# Create your views here.

def home(request):
    return render(request, 'index.html')

def todo(request):
    works = TodoModel.Objects.all()
    return render(request, 'todo.html', {'todos' : works})

