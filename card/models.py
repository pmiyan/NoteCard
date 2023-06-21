from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CardTitle(models.Model):
    title = models.TextField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"Card title is {self.title}")

class CardContent(models.Model):
    content = models.TextField(max_length=2000)
    title = models.OneToOneField(CardTitle, on_delete=models.CASCADE)

    def __str__(self):
        return (f"Card content is {self.content}")

class CardType(models.Model):
    category = models.TextField(max_length=100)
    color = models.CharField(max_length=10)
    title = models.ManyToManyField(CardTitle)

    def __str__(self):
        return (f"Card type is {self.category} of color {self.color}")