from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class CardType(models.Model):
    category = models.TextField(max_length=100)
    color = models.CharField(max_length=10)

    def __str__(self):
        return (f"Card type is {self.category} of color {self.color}")

class CardContent(models.Model):
    content = models.TextField(max_length=2000)

    def __str__(self):
        return (f"Card content is {self.content}")

class CardTitle(models.Model):
    title = models.TextField(max_length=500)
    content = models.OneToOneField(CardContent, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(CardType)

    def __str__(self):
        return (f"Card title is {self.title}")
    
    def get_absolute_url(self):
        return reverse('card-detail', kwargs={'card_id':self.pk})
    
