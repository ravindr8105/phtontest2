# Generated by Django 4.1.1 on 2024-06-08 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websitekoshfin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_subs', models.EmailField(max_length=254)),
            ],
        ),
    ]
