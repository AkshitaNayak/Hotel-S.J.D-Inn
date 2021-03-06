# Generated by Django 3.1 on 2020-08-09 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_property_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='category/')),
            ],
        ),
    ]
