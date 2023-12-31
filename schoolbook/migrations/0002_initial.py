# Generated by Django 5.0 on 2024-01-06 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schoolbook', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolbook',
            name='grade',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.SET_DEFAULT, to='user.grade'),
        ),
        migrations.AddField(
            model_name='module',
            name='school_books',
            field=models.ManyToManyField(to='schoolbook.schoolbook'),
        ),
        migrations.AddField(
            model_name='schoolbook',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolbook.subject'),
        ),
    ]
