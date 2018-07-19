# Generated by Django 2.0.4 on 2018-06-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicer',
            name='rating',
            field=models.PositiveSmallIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='servicer',
            name='serviced',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='servicer',
            name='email_id',
            field=models.EmailField(max_length=50),
        ),
    ]
