# Generated by Django 5.1.3 on 2024-12-03 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='target_update',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='file',
            name='update_script',
            field=models.URLField(),
        ),
    ]
