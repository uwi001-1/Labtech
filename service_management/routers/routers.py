from rest_framework.routers import DefaultRouter
from ..viewsets.service_viewsets import serviceViewsets
router = DefaultRouter()
router.register('service_management', serviceViewsets, basename='serviceViewsets')