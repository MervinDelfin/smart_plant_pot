
from rest_framework import routers, serializers, viewsets
from .models import State, DefindedState, Message
from django.utils import timezone
from datetime import timedelta
from sienkiewicza114Project.celery import send_bot_ai_message
from duty.models import Persons

router = routers.DefaultRouter()
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def create(self, request):

        water_min = DefindedState.objects.get(name="min").moisture
        if int(request.data['moisture'])/1024*100 < water_min and (
            Message.objects.exists() and
            Message.objects.latest('date').date < timezone.now() - timedelta(hours=2)
        ):
            print("Moisture is too low, please water the plant!")

            Message.objects.create(message=f"Moisture is too low, please water the plant! {int(request.data['moisture'])/1024*100}%")

            send_bot_ai_message.delay(f"Jesteś botem przypominającym o podlewaniu bazylii. Poziom wilgotności w ziemi własnie spadł poniżej {water_min}% i trzeba podlać roślinę. Napisz śmieszną wiadomość, która przypomni o podlaniu rośliny.", [Persons.objects.get(name="Marvin").chatfuel_id])

        return super().create(request)


router.register(r'states', StateViewSet, basename='states')

class DefinedStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefindedState
        fields = '__all__'

class DefinedStateViewSet(viewsets.ModelViewSet):
    queryset = DefindedState.objects.all()
    serializer_class = DefinedStateSerializer

router.register(r'defined_states', DefinedStateViewSet, basename='defined_states')