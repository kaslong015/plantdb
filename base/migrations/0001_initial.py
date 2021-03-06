# Generated by Django 3.2.9 on 2022-01-21 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('bioactive_compound', models.CharField(max_length=200, null=True)),
                ('uses', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scrape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=2080)),
            ],
        ),
    ]
