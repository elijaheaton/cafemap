# Generated by Django 4.2.11 on 2024-05-27 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafemap', '0002_alter_cafe_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]
