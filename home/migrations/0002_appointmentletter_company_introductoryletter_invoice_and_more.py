# Generated by Django 4.1.12 on 2023-10-31 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_address', models.CharField(max_length=100)),
                ('employee_city', models.CharField(max_length=100)),
                ('employee_pin_code', models.CharField(max_length=10)),
                ('employee_state', models.CharField(max_length=100)),
                ('employee_country', models.CharField(max_length=100)),
                ('employee_phone', models.CharField(max_length=15)),
                ('employee_email', models.EmailField(max_length=254)),
                ('joining_date', models.DateField()),
                ('designation', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_logo', models.ImageField(upload_to='company_logos/')),
                ('company_city', models.CharField(max_length=100)),
                ('company_pin_code', models.CharField(max_length=10)),
                ('company_state', models.CharField(max_length=100)),
                ('company_country', models.CharField(max_length=100)),
                ('company_phone', models.CharField(max_length=15)),
                ('company_email', models.EmailField(max_length=254)),
                ('company_cin', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IntroductoryLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=100)),
                ('candidate_city', models.CharField(max_length=100)),
                ('candidate_pin_code', models.CharField(max_length=10)),
                ('candidate_state', models.CharField(max_length=100)),
                ('candidate_country', models.CharField(max_length=100)),
                ('candidate_phone', models.CharField(max_length=15)),
                ('candidate_email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=100)),
                ('joining_date', models.DateField()),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('due_date', models.DateField(blank=True, null=True)),
                ('message', models.TextField(default='this is a default message.')),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.TextField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='OfferLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=100)),
                ('candidate_city', models.CharField(max_length=100)),
                ('candidate_pin_code', models.CharField(max_length=10)),
                ('candidate_state', models.CharField(max_length=100)),
                ('candidate_country', models.CharField(max_length=100)),
                ('candidate_phone', models.CharField(max_length=15)),
                ('candidate_email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=100)),
                ('joining_date', models.DateField()),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
