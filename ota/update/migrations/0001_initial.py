# Generated by Django 5.1.3 on 2024-12-03 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('device', '0001_initial'),
        ('version', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VersionUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[('SUCCESS', 1), ('FAILED', 2), ('IN_PROGRESS', 3)], default=3)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
                ('update', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='update.update')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version.version')),
            ],
        ),
        migrations.AddField(
            model_name='update',
            name='versions',
            field=models.ManyToManyField(through='update.VersionUpdate', to='device.device'),
        ),
    ]
