# Generated by Django 5.0.6 on 2024-08-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('task', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('due_date', models.DateTimeField()),
            ],
        ),
    ]
