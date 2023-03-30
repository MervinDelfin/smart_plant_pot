
from rest_framework import routers, serializers, viewsets
from .models import State, DefindedState

router = routers.DefaultRouter()
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

router.register(r'states', StateViewSet, basename='states')

class DefinedStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefindedState
        fields = '__all__'

class DefinedStateViewSet(viewsets.ModelViewSet):
    queryset = DefindedState.objects.all()
    serializer_class = DefinedStateSerializer

router.register(r'defined_states', DefinedStateViewSet, basename='defined_states')