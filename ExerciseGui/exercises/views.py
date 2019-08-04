from django.shortcuts import get_object_or_404, render
from django.views import generic

appRoot = "exercises/"

class IndexView(generic.ListView):
    template_name = appRoot+'index.html'

def areaofarectangularroom(request):
    return render(request, appRoot+'{}areaofarectangularroom.html')
