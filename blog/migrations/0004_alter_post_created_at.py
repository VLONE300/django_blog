# Generated by Django 5.0.3 on 2024-03-08 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 8, 6, 42, 57, 606934, tzinfo=datetime.timezone.utc)),
        ),
    ]
