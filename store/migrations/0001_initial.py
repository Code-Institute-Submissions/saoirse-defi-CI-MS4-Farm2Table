# Generated by Django 3.2.7 on 2021-10-29 17:41

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_ibanfield.fields
import image_optimizer.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('iban', django_ibanfield.fields.IBANField(max_length=35)),
                ('street_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('town', models.CharField(blank=True, max_length=40, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', image_optimizer.fields.OptimizedImageField(blank=True, null=True, upload_to='')),
                ('organic', models.BooleanField(default=False)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('county', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.county')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='profile.userprofile')),
            ],
        ),
    ]
