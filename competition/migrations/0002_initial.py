# Generated by Django 4.2 on 2023-12-10 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.grade'),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.subject'),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.question'),
        ),
        migrations.AddField(
            model_name='competition',
            name='grades',
            field=models.ManyToManyField(to='user.grade'),
        ),
        migrations.AddField(
            model_name='competition',
            name='subjects',
            field=models.ManyToManyField(to='competition.subject'),
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
            model_name='attempt',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='competition.subject'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
