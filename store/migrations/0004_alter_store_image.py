# Generated by Django 3.2.7 on 2021-11-05 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_county_friendly_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
