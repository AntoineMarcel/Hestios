# Generated by Django 2.0 on 2019-05-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_villes_shiva'),
    ]

    operations = [
        migrations.AddField(
            model_name='villes',
            name='maisonetservices',
            field=models.BooleanField(default=False),
        ),
    ]
