from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Ticket(models.Model):
    titre = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de création")
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
   
    class Meta:
        ordering = ['date']
    def __str__(self):
        return self.auteur