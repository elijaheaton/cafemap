from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Cafe

def index(request):
    cafes = Cafe.objects.order_by("name")
    return HttpResponse("Cafes:\n{cafes}")

def cafe(request, id):
    response = f"This is cafe {id}"
    print(response)
    cafe = get_object_or_404(Cafe, pk=id)
    return render(request, 'cafemap/cafe.html', {'cafe': cafe})
