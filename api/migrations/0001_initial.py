# Generated by Django 4.2.16 on 2024-10-30 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('start_point', models.CharField(max_length=100)),
                ('end_point', models.CharField(max_length=100)),
                ('distance', models.FloatField()),
                ('average_travel_time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('stop_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location_coordinates', models.CharField(max_length=100)),
                ('zone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('operator', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('day_of_week', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=50)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.route')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='RealTimeLocation',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('speed', models.FloatField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.route')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('prediction_id', models.AutoField(primary_key=True, serialize=False)),
                ('predicted_arrival_time', models.DateTimeField()),
                ('confidence_score', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stop')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalData',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('actual_arrival_time', models.DateTimeField()),
                ('timestamp', models.DateTimeField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.route')),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stop')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle')),
            ],
        ),
    ]