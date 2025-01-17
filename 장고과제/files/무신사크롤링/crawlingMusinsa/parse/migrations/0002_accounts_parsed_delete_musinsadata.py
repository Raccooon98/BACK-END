# Generated by Django 4.0.4 on 2022-07-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'accounts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parsed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(blank=True, null=True)),
                ('ranking', models.CharField(blank=True, max_length=10, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('item', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=30, null=True)),
                ('likes', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'parsed',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='musinsaData',
        ),
    ]
