# Generated by Django 5.1.3 on 2024-12-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'dice',
            },
        ),
    ]
