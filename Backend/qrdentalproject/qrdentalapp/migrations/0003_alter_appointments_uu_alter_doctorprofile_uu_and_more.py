# Generated by Django 5.0.2 on 2024-03-27 15:58

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrdentalapp', '0002_alter_appointments_uu_alter_doctorprofile_uu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='uu',
            field=models.UUIDField(default=uuid.UUID('afb0decb-fea8-4dc6-897d-b1117ff6e580'), unique=True),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='uu',
            field=models.UUIDField(default=uuid.UUID('c1322cfa-8f77-4243-a14a-3b94df44412b'), unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='uu',
            field=models.UUIDField(unique=True),
        ),
        migrations.AlterField(
            model_name='reciept',
            name='uu',
            field=models.UUIDField(default=uuid.UUID('7660f074-c5c0-4c8e-8591-892875cd9307'), unique=True),
        ),
        migrations.AlterField(
            model_name='timeslots',
            name='uu',
            field=models.UUIDField(default=uuid.UUID('34969e63-509b-4ae6-8a04-1cb8e78689af'), unique=True),
        ),
        migrations.AlterField(
            model_name='treatments',
            name='uu',
            field=models.UUIDField(default=uuid.UUID('fd471763-b35b-4b3d-9218-9571909f2417'), unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='uu',
            field=models.UUIDField(default=uuid.UUID('952df02d-c115-4180-9c46-2b6f2f6341ac'), unique=True),
        ),
    ]