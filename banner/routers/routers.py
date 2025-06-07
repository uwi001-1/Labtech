from rest_framework.routers import DefaultRouter
from ..viewsets.banner_viewsets import bannerViewsets

router = DefaultRouter()

router.register('banner', bannerViewsets, basename="bannerViewsets")