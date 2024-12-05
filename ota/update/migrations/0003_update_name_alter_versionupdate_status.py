# Generated by Django 5.1.3 on 2024-12-04 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0002_alter_versionupdate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='versionupdate',
            name='status',
            field=models.IntegerField(choices=[(1, 'SUCCESS'), (2, 'FAILED'), (3, 'IN_PROGRESS'), (4, 'CREATED')], default=4),
        ),
    ]