from rest_framework.routers import DefaultRouter
from ..viewsets.inquiries_viewsets import inquiriesViewsets

router = DefaultRouter()

router.register('inquiries', inquiriesViewsets, basename="inquiriesViewsets")