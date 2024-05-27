from django.conf import settings
from .models import *

import re
import hashlib


def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def validate_new_user(form):
    email = form.cleaned_data['email']
    pwd = hash_password(form.cleaned_data['password'])
    conf_pwd = hash_password(form.cleaned_data['confirm_password'])

    regex = '^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+.[a-zA-Z]+$'

    if not re.fullmatch(regex, email):
        return -1

    if not check_exists(User, email):
        return -2

    if pwd != conf_pwd:
        return -3

    return 1

def check_exists(cls, id):
    try:
        if cls == User:
            return User.objects.get(email=id)
        elif cls == Cafe:
            return Cafe.objects.get(id=id)
        else:
            raise NotImplementedError('Bad Class')
    except Exception as e:
        print(e)
        return False