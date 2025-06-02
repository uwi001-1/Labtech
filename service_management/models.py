from django.db import models

# Create your models here.
class Service_management(models.Model):
    Name = models.CharField(max_length=255)
    # Category = models.ForeignKey
    Price = models.PositiveIntegerField()
    Description = models.TextField()

    def __str__(self):
        return self.Name
    