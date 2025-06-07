from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.
class Service_management(models.Model):
    CATEGORY = (
        ('bloodTest', 'Blood Test'),
        ('urineTest', 'Urine Test'),
        ('gulcoseTest', 'Gulcose Test'),
        ('biopsy', 'Biopsy'),
        ('lipidProfile', 'Lipid Profile'),
        ('liverFunctionTests', 'Liver Function Tests')
    )
    SUB_CATEGORY = (
        ('wbcTest', 'WBC Test'),
        ('rbcTest', 'RBC Test'),
        ('platelets', 'Platelets'),
    )

    name = models.CharField(max_length=255)
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, unique=True)

    category = models.CharField(max_length= 30, choices= CATEGORY)
    sub_Category = models.CharField(max_length=20, choices=SUB_CATEGORY)

    price = models.PositiveIntegerField()
    description = models.TextField()

    feature_image = models.ImageField(upload_to='feature_image/')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}-{str(self.public_id)[1:5]}{str(self.public_id)[-1:-5]}'
        super().save(*args, **kwargs)
