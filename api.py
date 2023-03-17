
from rest_framework import routers, serializers, viewsets
from .models import State

router = routers.DefaultRouter()
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

router.register(r'states', StateViewSet, basename='states')