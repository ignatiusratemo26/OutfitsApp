from django.shortcuts import render
from .models import Clothes

# Create your views here.
def home(request):
    clothes = Clothes.objects.all()  # Get all clothes objects
    context = {'clothes': clothes}
    return render(request, 'base/home.html', context)