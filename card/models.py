from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class CardType(models.Model):
    category = models.TextField(max_length=100)
    color = models.CharField(max_length=10)

    def __str__(self):
        return (f"{self.category}")

class CardTitle(models.Model):
    title = models.TextField(max_length=500)
    content = models.TextField(max_length=2000)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(CardType)

    def __str__(self):
        return (self.title)
    
    def get_absolute_url(self):
        return reverse('card-detail', kwargs={'pk':self.pk})
    
