# Generated by Django 3.1.2 on 2020-10-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201002_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
