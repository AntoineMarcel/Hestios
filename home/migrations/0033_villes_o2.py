# Generated by Django 2.0 on 2019-05-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_villes_jemepropose'),
    ]

    operations = [
        migrations.AddField(
            model_name='villes',
            name='o2',
            field=models.BooleanField(default=False),
        ),
    ]
