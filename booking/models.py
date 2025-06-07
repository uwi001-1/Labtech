from django.db import models
import uuid
from django.utils.text import slugify
from service_management.models import Service_management

# Create your models here.
class BookingManagement(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    PAYMENT = (
        ('paymentAtClinic', 'Payment At Clinic'),
        ('onlinePayment', 'Online Payment'),
    )

    full_name = models.CharField(max_length=255, blank=False)
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, unique=True)

    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.PositiveIntegerField(max_length=10)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=GENDER)
    date = models.DateField(auto_now_add=True)

    service = models.ForeignKey(Service_management, related_name='service', on_delete=models.CASCADE)

    payment_option = models.CharField(max_length=50, choices=PAYMENT)
    message = models.TextField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)