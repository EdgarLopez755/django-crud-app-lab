# Generated by Django 5.1.5 on 2025-02-04 03:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rating', models.CharField(choices=[('A', 'Amazing'), ('O', 'Okay'), ('B', 'Bad')], default='A', max_length=1)),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.park')),
            ],
        ),
    ]
