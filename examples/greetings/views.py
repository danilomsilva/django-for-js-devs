from rest_framework import viewsets

from .models import Greeting
from .serializers import GreetingSerializer


class GreetingViewSet(viewsets.ModelViewSet):
    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer
