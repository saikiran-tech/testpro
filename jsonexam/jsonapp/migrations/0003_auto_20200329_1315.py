# Generated by Django 3.0.2 on 2020-03-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapp', '0002_auto_20200329_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]