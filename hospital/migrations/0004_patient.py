# Generated by Django 3.0.4 on 2020-06-23 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_receptionist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=10)),
                ('phonenumber', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5)),
            ],
        ),
    ]
