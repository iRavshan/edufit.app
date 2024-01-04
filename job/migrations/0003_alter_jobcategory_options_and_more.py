# Generated by Django 5.0 on 2023-12-28 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_jobcategory_subcategories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobcategory',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='jobsubcategory',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='jobcategory',
            name='subcategories',
        ),
        migrations.AddField(
            model_name='jobsubcategory',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='job.jobcategory'),
            preserve_default=False,
        ),
    ]