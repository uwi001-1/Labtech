from rest_framework.routers import DefaultRouter
from ..viewsets.meet_viewsets import meetViewsets

router = DefaultRouter()

router.register('meet', meetViewsets, basename="meetViewsets")