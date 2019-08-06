from django.http import HttpResponse
from django.shortcuts import render

appRoot = "exercises/"

def index(request):
    return render(request, 'exercises/index.html')

def areaofarectangularroom(request):
    return render(request, appRoot+'areaofarectangularroom.html')