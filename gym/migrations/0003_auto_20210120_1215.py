# Generated by Django 3.1.5 on 2021-01-20 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_auto_20201101_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='emailID',
            new_name='emailid',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
