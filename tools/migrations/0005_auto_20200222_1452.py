# Generated by Django 2.2.10 on 2020-02-22 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0004_tools_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tools',
            options={'ordering': ['name']},
        ),
    ]
