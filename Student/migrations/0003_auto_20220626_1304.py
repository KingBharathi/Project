# Generated by Django 3.2.12 on 2022-06-26 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_studentmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudId', models.CharField(max_length=5)),
                ('StudName2', models.CharField(max_length=20)),
                ('Mark01', models.CharField(max_length=5)),
                ('Mark02', models.CharField(max_length=5)),
                ('Mark03', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='StudentMark',
        ),
    ]