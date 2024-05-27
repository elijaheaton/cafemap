from django.shortcuts import render, get_object_or_404, redirect

from .models import Cafe, User
from .forms import LoginForm, SignupForm

from .helpers import *

WEBSITE = 'http://127.0.0.1:8000/cafemap/'

def index(request):
    cafes = Cafe.objects.order_by("name")
    list_cafes = []
    for c in cafes:
        list_cafes.append({
            'name': c.name,
            'address_one': c.address.line_one(),
            'address_two': c.address.line_two(),
            'link': f'{WEBSITE}cafe/{c.id}'
        })
    print(list_cafes)
    return render(request, 'cafemap/cafes.html', {
        'cafes': list_cafes
    })

def cafe(request, id):
    response = f"This is cafe {id}"
    print(response)
    cafe = get_object_or_404(Cafe, pk=id)
    return render(request, 'cafemap/cafe.html', {'cafe': cafe})

def login(request):
    if request.method == 'GET':
        return render(request, 'cafemap/login.html', {})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = hash_password(form.cleaned_data['password'])
            user = User.objects.filter(email=email, password=password).first()
            if user:
                request.session['email'] = email
                return redirect(index)

        error_message = "Incorrect username or password."

        return render(request, 'cafemap/login.html', {
            "error_message": error_message
        })
    else:
        return None
    

def signup(request):
    if request.method == 'GET':
        return render(request, 'cafemap/signup.html', {})
    elif request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            val = validate_new_user(form)
            if val == -1:
                error_message = 'Not a valid email.'
            elif val == -2:
                error_message = 'Email already used.'
            elif val == -3:
                error_message = 'Passwords don\'t match.'
            else:
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                pwd = hash_password(form.cleaned_data['password'])

                User.objects.update_or_create(email=email, defaults={
                    'name': name,
                    'password': pwd,
                })

                request.session['email'] = email
                return redirect(index)
        else:
            error_message = 'Please fill out the entire form.'
        return render(request, 'cafemap/signup.html', {
            'error_message': error_message
        })
    else:
        return None