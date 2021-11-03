# Generated by Django 3.2.9 on 2021-11-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, null=True)),
                ('product_category', models.CharField(max_length=50, null=True)),
                ('product_rate', models.IntegerField()),
                ('product_details', models.CharField(max_length=200, null=True)),
                ('product_stoke', models.IntegerField()),
            ],
        ),
    ]