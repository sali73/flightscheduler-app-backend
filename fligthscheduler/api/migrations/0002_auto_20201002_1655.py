# Generated by Django 3.1.2 on 2020-10-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='capacity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='seats_available',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='seats_reserved',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
