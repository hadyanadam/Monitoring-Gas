# Generated by Django 3.0.1 on 2020-02-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_sensorgasmodel_no_tiang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorgasmodel',
            name='no_tiang',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3)], default=1, max_length=1),
        ),
    ]
