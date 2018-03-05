# Generated by Django 2.0.1 on 2018-01-24 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('profile_picture', models.CharField(max_length=500)),
                ('payment_method', models.CharField(max_length=50)),
                ('payment_token', models.CharField(max_length=150)),
            ],
        ),
    ]
