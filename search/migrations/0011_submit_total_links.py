# Generated by Django 2.1.15 on 2020-09-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_submit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='total_links',
            field=models.CharField(max_length=100000, null=True),
        ),
    ]
