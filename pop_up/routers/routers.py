from rest_framework.routers import DefaultRouter
from ..viewsets.pop_up_viewsets import popUpViewsets

router = DefaultRouter()

router.register('pop_up', popUpViewsets, basename="pop_upViewsets")