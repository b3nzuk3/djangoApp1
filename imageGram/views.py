from django.shortcuts import render


def home(request):
    return render(request, 'imageGram/base.html')
# Create your views here.
