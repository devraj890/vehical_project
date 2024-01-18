# Generated by Django 4.1.5 on 2023-04-03 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('feedbak_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complain_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('vehicle_make', models.CharField(max_length=100)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_year', models.IntegerField()),
                ('licence_plate', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('complain_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('date_of_theft', models.DateField()),
                ('time_of_theft', models.TimeField()),
                ('location_last_seen', models.CharField(max_length=200)),
                ('rc_no', models.CharField(max_length=50)),
                ('old_vehicle_shell', models.TextField(blank=True)),
                ('is_found', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
