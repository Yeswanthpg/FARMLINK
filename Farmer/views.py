from django.shortcuts import render

# Create your views here.

def Farmer(request):
    return render(request, 'farmer/marketplace.html')