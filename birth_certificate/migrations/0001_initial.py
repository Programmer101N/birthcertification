# Generated by Django 4.0.3 on 2022-05-16 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fullname', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('mothername', models.CharField(max_length=100)),
                ('place_of_birth', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=100)),
                ('time', models.TimeField(blank=True)),
                ('date', models.DateField(blank=True)),
            ],
        ),
    ]
