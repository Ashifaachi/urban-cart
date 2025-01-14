from django.shortcuts import render
from apps.admin1.models import Slider

# Create your views here.
from django.shortcuts import render, get_object_or_404


def index(request):
   sliders = Slider.objects.all()
   return render(request, 'home/index.html',{'sliders':sliders})
