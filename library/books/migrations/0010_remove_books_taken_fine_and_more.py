# Generated by Django 5.0 on 2023-12-18 23:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_books_taken_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books_taken',
            name='fine',
        ),
        migrations.AlterField(
            model_name='books_taken',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 23, 53, 22, 807023, tzinfo=datetime.timezone.utc)),
        ),
    ]
