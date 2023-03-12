from django.shortcuts import render
from django.contrib.auth import get_user_model
# from django.contrib.auth.decorators import login_required


User = get_user_model


def index(request):
    return render(request, 'matches/index.html')
