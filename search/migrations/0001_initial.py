# Generated by Django 2.1.15 on 2020-09-19 10:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='submit',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name=uuid.uuid4)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=20000)),
                ('pages', models.CharField(max_length=30000)),
            ],
        ),
    ]
