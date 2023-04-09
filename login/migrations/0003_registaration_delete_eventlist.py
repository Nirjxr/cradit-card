# Generated by Django 4.1.7 on 2023-02-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_eventlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('age', models.PositiveIntegerField()),
                ('number', models.CharField(max_length=12)),
                ('alt_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Registration',
            },
        ),
        migrations.DeleteModel(
            name='EventList',
        ),
    ]
