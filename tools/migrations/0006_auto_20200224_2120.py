# Generated by Django 2.2.10 on 2020-02-24 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_auto_20200222_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='available',
            field=models.CharField(choices=[('AVAILABLE', 'Available'), ('NOT AVAILABLE', 'Not Available')], max_length=255),
        ),
    ]