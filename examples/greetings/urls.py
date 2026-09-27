from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import GreetingViewSet, ping, whoami

router = DefaultRouter()
router.register("greetings", GreetingViewSet, basename="greeting")

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("auth/token/", obtain_auth_token, name="obtain-token"),
    path("whoami/", whoami, name="whoami"),
    *router.urls,
]
