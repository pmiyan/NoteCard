# Generated by Django 4.2.2 on 2023-06-19 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardtitle',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]