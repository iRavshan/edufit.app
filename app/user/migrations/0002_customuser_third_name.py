# Generated by Django 5.0 on 2023-12-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='third_name',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
