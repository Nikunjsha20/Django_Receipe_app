# Generated by Django 5.0.6 on 2025-03-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=100)),
                ('receipe_description', models.TextField(max_length=200)),
                ('receipe_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
