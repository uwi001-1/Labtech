from rest_framework.routers import DefaultRouter
from ..viewsets.booking_viewsets import bookingViewsets

router = DefaultRouter()

router.register('booking', bookingViewsets, basename="bookingViewsets")