# Generated by Django 5.0.1 on 2024-03-04 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 4, 16, 19, 2, 383358, tzinfo=datetime.timezone.utc)),
        ),
    ]
