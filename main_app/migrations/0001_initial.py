# Generated by Django 3.0.6 on 2021-01-19 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=20)),
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('r_id', models.AutoField(primary_key=True, serialize=False)),
                ('starts', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=1)),
                ('description', models.CharField(max_length=300)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.car')),
            ],
        ),
    ]
