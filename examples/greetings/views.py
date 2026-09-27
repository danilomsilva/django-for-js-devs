from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Greeting
from .permissions import IsStaffOrReadOnly
from .serializers import GreetingSerializer


@api_view(["GET"])
def ping(request):
    """Function-based view — the simplest possible Django REST endpoint."""
    return Response({"status": "ok"})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def whoami(request):
    """Requires authentication (session or token, see settings.py). Used in
    docs/12-auth.md and docs/13-permissions.md to demonstrate auth end to end.
    """
    return Response({"username": request.user.username})


class GreetingViewSet(viewsets.ModelViewSet):
    """Class-based view — handles list/create/retrieve/update/delete for
    Greeting in one class, wired to a full CRUD URL set via the router.
    """

    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer
    permission_classes = [IsStaffOrReadOnly]
    filterset_fields = ["category__name"]
    ordering_fields = ["created_at", "message"]
