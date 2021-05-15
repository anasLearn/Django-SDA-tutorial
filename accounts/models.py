from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.user.first_name} {self.user.last_name}"