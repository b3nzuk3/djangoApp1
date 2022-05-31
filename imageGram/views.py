from django.shortcuts import render
from .models import Image



def home(request):
    images=Image.objects.all()
    ctx = {'images': images}

    return render(request, 'imageGram/home.html', ctx)
# Create your views here.
