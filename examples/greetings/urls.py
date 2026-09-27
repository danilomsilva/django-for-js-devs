from rest_framework.routers import DefaultRouter

from .views import GreetingViewSet

router = DefaultRouter()
router.register("greetings", GreetingViewSet, basename="greeting")

urlpatterns = router.urls
