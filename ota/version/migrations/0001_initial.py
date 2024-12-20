# Generated by Django 5.1.3 on 2024-12-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('files', models.ManyToManyField(to='file.file')),
            ],
        ),
    ]
