# Generated by Django 3.1.4 on 2023-02-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('flag', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('code', models.IntegerField(blank=True, default=0, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
