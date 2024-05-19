from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Cafe

WEBSITE = 'http://127.0.0.1:8000/cafemap/'

def index(request):
    cafes = Cafe.objects.order_by("name")
    list_cafes = []
    for c in cafes:
        list_cafes.append({'name': c.name, 'link': f'{WEBSITE}cafe/{c.id}'})
    print(list_cafes)
    return render(request, 'cafemap/cafes.html', {
        'cafes': list_cafes
    })

def cafe(request, id):
    response = f"This is cafe {id}"
    print(response)
    cafe = get_object_or_404(Cafe, pk=id)
    return render(request, 'cafemap/cafe.html', {'cafe': cafe})
