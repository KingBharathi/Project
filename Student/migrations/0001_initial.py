# Generated by Django 3.2.12 on 2022-06-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudId', models.CharField(max_length=5)),
                ('StudName', models.CharField(max_length=20)),
                ('StudPhone', models.CharField(max_length=10)),
            ],
        ),
    ]
