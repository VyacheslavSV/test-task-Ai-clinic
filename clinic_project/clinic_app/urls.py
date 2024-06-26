from django.urls import path, include
from rest_framework import routers

from clinic_app.views import TeamViewSet, PersonViewSet

router = routers.SimpleRouter()

router.register(r'teams', TeamViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
