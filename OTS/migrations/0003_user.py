# Generated by Django 3.2.9 on 2022-02-18 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTS', '0002_auto_20220215_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=15)),
            ],
        ),
    ]
