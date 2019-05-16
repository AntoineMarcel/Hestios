# Generated by Django 2.0 on 2019-05-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_delete_villes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Villes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=30, unique=True)),
                ('cp', models.CharField(max_length=5, verbose_name='Code Postale')),
                ('deliveroo', models.BooleanField(default=False)),
                ('ubereat', models.BooleanField(default=False, verbose_name='Uber Eat')),
                ('justeat', models.BooleanField(default=False, verbose_name='Just Eat')),
            ],
            options={
                'ordering': ['ville'],
            },
        ),
    ]
