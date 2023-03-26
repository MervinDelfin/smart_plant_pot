from django.shortcuts import render
from .models import State, DefindedState
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseBadRequest

def format_last_seen_text(last_online):
    time_since_online = timezone.now() - last_online
    days = (timezone.now().date() - last_online.date()).days
    hours, remainder = divmod(time_since_online.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if days>0:
        if days==1:
            last_online_text = f"wczoraj {timezone.localtime(last_online).strftime('%H:%M')}"
        else:
            last_online_text = f"{days} dni temu, {timezone.localtime(last_online).strftime('%H:%M')}"
    elif hours>0:
        last_online_text = f"dzisiaj {timezone.localtime(last_online).strftime('%H:%M')}"
    elif minutes>0:
        last_online_text = f"{minutes} min temu"
    else:
        last_online_text = "teraz"
    return last_online_text

# Create your views here.
def index(request):
    state = State.objects.order_by('-date').first()
    
    try:
        water_min = DefindedState.objects.get(name="min").moisture
        water_max = DefindedState.objects.get(name="max").moisture
    except ObjectDoesNotExist:
        return HttpResponseBadRequest("Ustaw najpierw minimalaną i maksymalną wartość")


    return render(request, 'smart_plant_pot/index.html', {'water_level': state.moisture/1024*100, 'water_max':water_max, 'water_min': water_min, 'update_time': format_last_seen_text(state.date)})