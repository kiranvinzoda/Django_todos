# Generated by Django 4.1.4 on 2022-12-26 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
