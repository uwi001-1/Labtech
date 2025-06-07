from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.
class CustomerInquiries(models.Model):
    full_name = models.CharField(max_length=255)
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, unique=True)

    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.PositiveIntegerField(max_length=10)
    message = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.full_name)}-{str(self.public_id)[1:5]}{str(self.public_id)[-1:-5]}'
        super().save(*args, **kwargs)