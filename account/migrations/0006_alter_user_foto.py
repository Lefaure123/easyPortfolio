# Generated by Django 4.1 on 2022-09-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_modpass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='./Pictures'),
        ),
    ]