# Generated by Django 5.0.2 on 2024-02-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DonationApp', '0003_rename_userpic_donor_donorpic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donorname', models.CharField(max_length=50, null=True)),
                ('donationname', models.CharField(max_length=50, null=True)),
                ('donationpic', models.FileField(null=True, upload_to='')),
                ('collectionloc', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('donationdate', models.DateTimeField(auto_now_add=True)),
                ('adminremark', models.CharField(max_length=20, null=True)),
                ('volunteerassign', models.CharField(max_length=20, null=True)),
                ('donationarea', models.CharField(max_length=50, null=True)),
                ('volunteerremark', models.CharField(max_length=20, null=True)),
                ('updationdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonationArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaname', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='volunteer',
            name='adminremark',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='idpic',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]