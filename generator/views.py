from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,template_name='generator/home.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstyvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('specialchar'):
        characters.extend(list('!$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    length = int(request.GET.get('length'))

    thepass=''

    for x in range(length):
        thepass += random.choice(characters)


    return render(request, 'generator/password.html', {'pass':thepass})

def about(request):
    return render(request, 'generator/about.html')