# Generated by Django 3.1.7 on 2021-04-07 12:47

from django.db import migrations, models
import dlearn.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LearnersPermit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_id', models.CharField(max_length=15)),
                ('permit_id', models.CharField(default=dlearn.models.generate_id, max_length=15)),
                ('licence_class', models.CharField(max_length=10)),
                ('given_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('postal_address', models.CharField(max_length=255)),
            ],
        ),
    ]
