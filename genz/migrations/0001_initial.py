# Generated by Django 3.0.2 on 2020-02-01 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=12)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('description', models.TextField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genz.Shop')),
            ],
        ),
    ]