# Generated by Django 4.2.4 on 2023-09-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numberapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('img1', models.ImageField(upload_to='pic')),
                ('des', models.TextField()),
            ],
        ),
    ]
