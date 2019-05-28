# Generated by Django 2.2.1 on 2019-05-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibroker', '0002_auto_20190528_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]