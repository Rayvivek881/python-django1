# Generated by Django 4.2.1 on 2023-05-27 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_testmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testmodel',
            old_name='ProductID',
            new_name='Product',
        ),
    ]
