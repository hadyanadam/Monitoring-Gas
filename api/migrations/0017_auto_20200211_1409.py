# Generated by Django 3.0.1 on 2020-02-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200211_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorgasmodel',
            name='no_tiang',
            field=models.CharField(choices=[('Tiang A', 'A'), ('Tiang B', 'B'), ('Tiang C', 'C')], default=None, max_length=10),
        ),
    ]
