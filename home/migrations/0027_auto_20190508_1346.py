# Generated by Django 2.0 on 2019-05-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20190508_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturation',
            name='facture',
            field=models.FileField(upload_to='home/factures/'),
        ),
    ]
