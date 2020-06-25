# Generated by Django 3.0.7 on 2020-06-22 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=20)),
                ('event_head_id', models.IntegerField()),
                ('event_desc', models.CharField(max_length=500)),
                ('event_location', models.CharField(max_length=30)),
                ('event_dept', models.CharField(max_length=10)),
                ('budget_expected', models.IntegerField()),
                ('actual_budget', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='registrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]