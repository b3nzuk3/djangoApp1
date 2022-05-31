from django.shortcuts import render


def home(request):
    return render(request, 'imageGram/home.html')
# Create your views here.
