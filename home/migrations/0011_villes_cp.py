# Generated by Django 2.0 on 2019-05-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190501_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='villes',
            name='cp',
            field=models.CharField(default='', max_length=5, verbose_name='Code Postale'),
            preserve_default=False,
        ),
    ]
