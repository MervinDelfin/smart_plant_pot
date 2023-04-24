from django.shortcuts import render
from .models import State, DefindedState
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse

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
        DefindedState.objects.create(name="min", moisture=30).save()
        DefindedState.objects.create(name='max', moisture=60).save()


    return render(request, 'smart_plant_pot/index.html', {'water_level': state.moisture/1024*100, 'water_max':water_max, 'water_min': water_min, 'update_time': format_last_seen_text(state.date)})



def settings(request):
    water_min = DefindedState.objects.get(name="min").moisture
    water_max = DefindedState.objects.get(name="max").moisture
    return render(request, 'smart_plant_pot/settings.html', {'water_max':water_max, 'water_min': water_min})


def setDefinedStates(request):
    if request.method != "POST" or 'min' not in request.POST or 'max' not in request.POST:
        return HttpResponseBadRequest("bad request")
    
    water_min = DefindedState.objects.get(name="min")
    water_min.moisture = int(request.POST['min'])
    water_min.save()

    water_max = DefindedState.objects.get(name="max")
    water_max.moisture = int(request.POST['max'])
    water_max.save()

    return HttpResponseRedirect(reverse('smart_plant_pot:index'))

    
def chart(requst):

    state = State.objects.order_by('-date').first()

    context = {
        'data': State.objects.order_by('-date')[:10000:-100],
        'update_time': format_last_seen_text(state.date)
    }

    return render(requst, 'smart_plant_pot/chart.html', context)
