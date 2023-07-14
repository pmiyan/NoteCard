from django.contrib import admin
from .models import CardTitle
from .models import CardType

admin.site.register(CardTitle)
admin.site.register(CardType)