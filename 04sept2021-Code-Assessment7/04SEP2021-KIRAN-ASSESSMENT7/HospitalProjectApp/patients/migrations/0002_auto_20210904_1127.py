# Generated by Django 3.2.6 on 2021-09-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(blank='True', default='No Name', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='username',
            field=models.CharField(blank='True', default='No Name', max_length=50),
        ),
    ]
