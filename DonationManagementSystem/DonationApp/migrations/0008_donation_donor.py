# Generated by Django 5.0.2 on 2024-03-07 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DonationApp', '0007_donor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DonationApp.donor'),
        ),
    ]
