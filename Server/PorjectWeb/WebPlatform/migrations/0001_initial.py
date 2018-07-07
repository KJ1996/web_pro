# Generated by Django 2.0.4 on 2018-05-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oderNumber', models.IntegerField()),
                ('student', models.CharField(max_length=20)),
                ('waterman', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=13)),
                ('interval', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('allocation', models.IntegerField()),
                ('complete', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('identity', models.IntegerField()),
            ],
        ),
    ]
