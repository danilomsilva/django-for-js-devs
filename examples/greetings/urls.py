from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import GreetingViewSet, ping

router = DefaultRouter()
router.register("greetings", GreetingViewSet, basename="greeting")

urlpatterns = [
    path("ping/", ping, name="ping"),
    *router.urls,
]
