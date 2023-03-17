from django.shortcuts import render
from .models import State

# Create your views here.
def index(request):
    state = State.objects.order_by('-date').first()
    return render(request, 'smart_plant_pot/index.html', {'water_level': state.moisture/1024*100, 'water_max':60, 'water_min': 30})