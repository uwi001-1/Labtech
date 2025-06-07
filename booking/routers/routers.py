from rest_framework.routers import DefaultRouter
from ..viewsets.booking_viewsets import bookingManagementViewsets

router = DefaultRouter()

router.register('bookingManagement', bookingManagementViewsets, basename="bookingViewsets")