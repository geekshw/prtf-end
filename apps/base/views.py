from django.shortcuts import render
from .models import Index  # предположим, что у вас есть модель Index

def index(request):
    try:
        index_object = Index.objects.get(id=1)  # Пример запроса
    except Index.DoesNotExist:
        index_object = None
    return render(request, 'index.html', {'index_object': index_object})


def home(request):
    index = Index.objects.first()  
    return render(request, 'index.html', {'index': index})


