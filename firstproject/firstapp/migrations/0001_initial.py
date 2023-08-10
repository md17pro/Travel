# Generated by Django 4.1.7 on 2023-04-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
