# Generated by Django 3.1.4 on 2021-01-13 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_app', '0002_auto_20210112_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='User',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
