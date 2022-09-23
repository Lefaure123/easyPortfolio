# Generated by Django 4.1 on 2022-09-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('non', models.CharField(max_length=50)),
                ('siyati', models.CharField(max_length=50)),
                ('imel', models.EmailField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='pictures/')),
                ('telefon', models.CharField(max_length=60)),
            ],
        ),
    ]