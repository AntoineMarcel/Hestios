# Generated by Django 2.0 on 2019-05-07 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_villes_allovoisin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villes',
            name='cp',
            field=models.CharField(max_length=5, verbose_name='Code Postale'),
        ),
    ]
