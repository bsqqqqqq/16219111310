# Generated by Django 2.1.7 on 2019-04-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0004_weathers'),
    ]

    operations = [
        migrations.CreateModel(
            name='phones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mNo', models.CharField(max_length=32)),
                ('mMark', models.CharField(max_length=256)),
                ('mPrice', models.CharField(max_length=32)),
                ('mNote', models.CharField(max_length=1024)),
                ('mFile', models.CharField(max_length=256)),
            ],
        ),
    ]
