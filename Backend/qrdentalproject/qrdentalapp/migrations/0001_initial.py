# Generated by Django 5.0.2 on 2024-02-20 14:45

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu', models.UUIDField(default=uuid.UUID('c534af4a-78e4-46d1-b5f8-ce91cbe1a806'), unique=True)),
                ('name', models.CharField(max_length=250)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('age', models.IntegerField()),
                ('qualification', models.CharField(max_length=250)),
                ('experience', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu', models.UUIDField(default=uuid.UUID('f643637e-3c83-44c6-96a1-60e8d16ff70d'), unique=True)),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=250)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('age', models.IntegerField()),
                ('adhaar_num', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('profile_qr', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Timeslots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu', models.UUIDField(default=uuid.UUID('d4946d9b-623d-4ec7-92f0-a3971853ff76'), unique=True)),
                ('date', models.DateField()),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('status', models.CharField(default='Available', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Treatments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu', models.UUIDField(default=uuid.UUID('6f228ab1-5eaf-448d-b753-4d09f194b32a'), unique=True)),
                ('name', models.CharField(max_length=250)),
                ('duration_minutes', models.IntegerField()),
                ('visibility_type', models.CharField(choices=[('1', 'Admin'), ('2', 'Receptionist'), ('3', 'Patient')], default='1', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu', models.UUIDField(default=uuid.UUID('b201049d-a23d-4b44-977c-04580a63a8d1'), unique=True)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=20)),
                ('user_type', models.CharField(choices=[('1', 'Admin'), ('2', 'Receptionist'), ('3', 'Patient')], default='3', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu', models.UUIDField(default=uuid.UUID('1e5f427a-64a6-4958-828e-309dcdc4910f'), unique=True)),
                ('patient_remark', models.TextField()),
                ('doctor_remark', models.TextField()),
                ('appointment_qr', models.FileField(upload_to='')),
                ('status', models.CharField(choices=[('P', 'Pending for approval'), ('C', 'Confirmed'), ('R', 'Request for change'), ('CL', 'Cancelled')], default='P', max_length=2)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qrdentalapp.patient')),
                ('time_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qrdentalapp.timeslots')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qrdentalapp.treatments')),
            ],
        ),
        migrations.CreateModel(
            name='Reciept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uu', models.UUIDField(default=uuid.UUID('d2a71d7f-57ad-4178-9270-d6ae9566c765'), unique=True)),
                ('reciept_date', models.DateField(auto_now_add=True)),
                ('paid_amount', models.FloatField()),
                ('payment_mode', models.CharField(choices=[('C', 'Cash'), ('O', 'Online')], max_length=1)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qrdentalapp.appointments')),
            ],
        ),
    ]