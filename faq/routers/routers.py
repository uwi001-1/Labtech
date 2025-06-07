from rest_framework.routers import DefaultRouter
from ..viewsets.faq_viewsets import faqViewsets

router = DefaultRouter()

router.register('faq', faqViewsets, basename="faqViewsets")