# Generated by Django 5.0.2 on 2024-02-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DonationApp', '0004_donation_donationarea_volunteer_adminremark_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
