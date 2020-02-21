from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


User = get_user_model()

class Tools(models.Model):

    AVAILABLE = 'AVAILABLE'
    NOT_AVAILABLE = 'NOT_AVAILABLE'

    AVAILABLE_CHOICES = [
        (AVAILABLE, 'Available'),
        (NOT_AVAILABLE, 'Not Available')
    ]

    name = models.CharField(max_length=255)
    picture = models.URLField(null=True)
    available = models.CharField(max_length=255, choices=AVAILABLE_CHOICES)
    price = models.IntegerField(null=True)
    neighbor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
