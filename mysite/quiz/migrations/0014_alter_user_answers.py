# Generated by Django 4.0.2 on 2022-03-16 12:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_useranswer_alter_user_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='answers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None),
        ),
    ]
