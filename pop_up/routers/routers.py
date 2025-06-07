from rest_framework.routers import DefaultRouter
from ..viewsets.pop_up_viewsets import pop_upViewsets

router = DefaultRouter()

router.register('pop_up', pop_upViewsets, basename="pop_upViewsets")