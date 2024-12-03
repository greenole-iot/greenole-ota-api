# Generated by Django 4.2.13 on 2024-12-03 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_alter_file_target_update_alter_file_update_script'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='target_update',
        ),
        migrations.RemoveField(
            model_name='file',
            name='update_script',
        ),
        migrations.AddField(
            model_name='file',
            name='target_update_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='file',
            name='target_update_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='update_script_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='file',
            name='update_script_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
