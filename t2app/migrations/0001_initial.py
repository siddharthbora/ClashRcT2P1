# Generated by Django 3.1 on 2020-08-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phoneNo', models.CharField(max_length=11)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]
