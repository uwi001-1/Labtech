from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.
class BannerText(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, unique=True)

    image_file = models.ImageField(upload_to='hero_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    video_file = models.FileField(upload_to='video/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)