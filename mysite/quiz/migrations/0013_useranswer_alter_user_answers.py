# Generated by Django 4.0.2 on 2022-03-16 12:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_user_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField(default=0)),
                ('choice', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='answers',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None), default=list, size=None),
        ),
    ]
