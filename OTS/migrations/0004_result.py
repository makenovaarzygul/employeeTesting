# Generated by Django 3.2.12 on 2022-03-01 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OTS', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_attempt', models.IntegerField()),
                ('total_wrong', models.IntegerField()),
                ('total_right', models.IntegerField()),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OTS.user')),
            ],
        ),
    ]
