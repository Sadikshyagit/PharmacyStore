# Generated by Django 4.1.7 on 2023-03-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default=0, max_length=40, null=0)),
                ('dob', models.DateField(default=0, max_length=20)),
                ('email', models.EmailField(max_length=10)),
                ('password', models.CharField(default=0, max_length=50, null=0)),
                ('cpassword', models.CharField(default=0, max_length=50, null=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]