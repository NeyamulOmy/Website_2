# Generated by Django 3.0.8 on 2020-07-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200728_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
