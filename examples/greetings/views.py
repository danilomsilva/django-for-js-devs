from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Greeting
from .serializers import GreetingSerializer


@api_view(["GET"])
def ping(request):
    """Function-based view — the simplest possible Django REST endpoint."""
    return Response({"status": "ok"})


class GreetingViewSet(viewsets.ModelViewSet):
    """Class-based view — handles list/create/retrieve/update/delete for
    Greeting in one class, wired to a full CRUD URL set via the router.
    """

    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer
