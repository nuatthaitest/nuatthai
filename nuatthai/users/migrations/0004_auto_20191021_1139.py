# Generated by Django 2.2.6 on 2019-10-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_services_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='services',
            name='service',
            field=models.CharField(choices=[(350, 'Nuat Thai Foot Massage(1hour)'), (350, 'Thai Body massage w/ Oil(1hour)'), (400, 'Sweddish Massage(1hour)'), (400, 'Armoatherapy Massage(1hour)'), (250, 'Express - Back and Head(30 mins)'), (250, 'Foot Massage(30 mins)'), (250, 'Back Massage(30 mins)'), (250, 'Head massage(30 mins)')], max_length=1),
        ),
    ]
