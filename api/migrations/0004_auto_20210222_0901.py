# Generated by Django 3.0 on 2021-02-22 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210222_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='notes',
            field=models.CharField(max_length=500),
        ),
    ]
