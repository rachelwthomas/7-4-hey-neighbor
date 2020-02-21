from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Tools(models.Model):
    name = models.CharField(max_length=255)
    picture = models.URLField(null=True)
    price = models.IntegerField(null=True)
    neighbor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
