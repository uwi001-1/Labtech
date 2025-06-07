from rest_framework.routers import DefaultRouter
from ..viewsets.meet_viewsets import meetTheTeamViewsets

router = DefaultRouter()

router.register('meet', meetTheTeamViewsets, basename="meetViewsets")