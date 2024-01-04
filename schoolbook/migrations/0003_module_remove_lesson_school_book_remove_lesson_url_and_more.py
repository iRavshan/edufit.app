# Generated by Django 5.0 on 2024-01-02 07:37

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0003_alter_attempt_options_alter_competition_options_and_more'),
        ('schoolbook', '0002_schoolbook_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='school_book',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='url',
        ),
        migrations.RemoveField(
            model_name='schoolbook',
            name='title',
        ),
        migrations.AddField(
            model_name='lesson',
            name='content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='video_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='schoolbook',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='competition.subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='schoolbook.module'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolbook',
            name='modules',
            field=models.ManyToManyField(to='schoolbook.module'),
        ),
    ]