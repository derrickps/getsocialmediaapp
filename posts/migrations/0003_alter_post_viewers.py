# Generated by Django 3.2.3 on 2021-05-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_viewers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='viewers',
            field=models.CharField(choices=[('Friends', 'Only Friends'), ('Public', 'Public')], max_length=14),
        ),
    ]
