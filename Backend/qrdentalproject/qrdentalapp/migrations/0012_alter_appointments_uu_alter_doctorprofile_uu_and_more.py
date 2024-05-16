# Generated by Django 5.0.2 on 2024-04-19 16:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrdentalapp', '0011_alter_appointments_uu_alter_doctorprofile_uu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='uu',
            field=models.UUIDField(default=uuid.UUID('fbe0bb00-f85f-4c21-aa21-bf1779a43c27'), unique=True),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='uu',
            field=models.UUIDField(default=uuid.UUID('d849eef3-caad-4448-bdab-82f019764c3f'), unique=True),
        ),
        migrations.AlterField(
            model_name='reciept',
            name='uu',
            field=models.UUIDField(default=uuid.UUID('9d42ab1c-5feb-4d3b-90c9-aec2a45d01fa'), unique=True),
        ),
        migrations.AlterField(
            model_name='timeslots',
            name='uu',
            field=models.UUIDField(default=uuid.UUID('60b5b92c-2524-4263-a8af-bbf8db597dc9'), unique=True),
        ),
        migrations.AlterField(
            model_name='treatments',
            name='uu',
            field=models.UUIDField(default=uuid.UUID('0ef613bc-b66e-4fa6-b34e-c58a7e105fbe'), unique=True),
        ),
    ]