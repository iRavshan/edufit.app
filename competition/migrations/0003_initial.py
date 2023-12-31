# Generated by Django 5.0 on 2024-01-06 04:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competition', '0002_initial'),
        ('schoolbook', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='competition',
            name='grades',
            field=models.ManyToManyField(to='user.grade'),
        ),
        migrations.AddField(
            model_name='competition',
            name='subjects',
            field=models.ManyToManyField(to='schoolbook.subject'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.competition'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='options',
            field=models.ManyToManyField(to='competition.option'),
        ),
        migrations.AddField(
            model_name='question',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='competition.competition'),
        ),
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.grade'),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolbook.subject'),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.question'),
        ),
    ]
