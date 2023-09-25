# Generated by Django 4.2.4 on 2023-08-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('card_id', models.CharField(blank=True, max_length=10, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_data', models.DateTimeField(auto_now=True, verbose_name='birth date')),
                ('expiration_data', models.DateTimeField(auto_now=True, verbose_name='expiration date')),
            ],
        ),
    ]