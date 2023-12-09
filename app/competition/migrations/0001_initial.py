# Generated by Django 5.0 on 2023-12-08 19:06

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_alter_customuser_phone_alter_customuser_third_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(max_length=100, unique=True)),
                ('subtitle', models.CharField(max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.grade')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.subject')),
            ],
        ),
    ]
