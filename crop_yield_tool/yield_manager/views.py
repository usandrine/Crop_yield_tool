from django.shortcuts import render

# Create your views here.
from .models import Crop, YieldRecord

def home(request):
    crops = Crop.objects.all()
    return render(request, 'yield_manager/home.html', {'crops': crops})

def crop_detail(request, crop_id):
    crop = Crop.objects.get(id=crop_id)
    return render(request, 'yield_manager/crop_detail.html', {'crop': crop})