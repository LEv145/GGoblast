# Generated by Django 4.1.2 on 2022-10-30 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0002_event_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='interest',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telephone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
