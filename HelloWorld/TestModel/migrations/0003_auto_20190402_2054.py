# Generated by Django 2.1.7 on 2019-04-02 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_auto_20190402_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='name',
            new_name='content',
        ),
    ]
