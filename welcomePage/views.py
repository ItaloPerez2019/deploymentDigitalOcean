from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'welcomePage/welcometwo.html' )


def intro(request):
    return render(request, 'welcomePage/introOne.html')