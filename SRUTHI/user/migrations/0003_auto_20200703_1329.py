# Generated by Django 3.0.7 on 2020-07-03 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200703_1329'),
        ('user', '0002_event_registrations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrations',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='registrations',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='registrations',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
