from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    keyboards = Keyboard.objects.all()
    context = {
        'keyboards': keyboards
    }
    return render(request, 'Listings/home.html', context)

def keyboard_detail_view(request, id):
    keyboard = Keyboard.objects.get(id= id)
    context = {
        'keyboard': keyboard
    }
    return render(request, 'Listings/keyboard_detail_view.html', context)