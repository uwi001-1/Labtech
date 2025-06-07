from rest_framework.routers import DefaultRouter
from ..viewsets.inquiries_viewsets import customerInquiriesViewsets

router = DefaultRouter()

router.register('inquiries', customerInquiriesViewsets, basename="inquiriesViewsets")