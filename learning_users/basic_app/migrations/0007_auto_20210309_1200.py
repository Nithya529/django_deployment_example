# Generated by Django 3.1.5 on 2021-03-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_auto_20210113_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]