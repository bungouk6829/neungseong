# Generated by Django 3.0.5 on 2020-11-13 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='information_post',
            table='information_posts',
        ),
        migrations.AlterModelTable(
            name='notice_post',
            table='notice_posts',
        ),
        migrations.AlterModelTable(
            name='result_post',
            table='result_posts',
        ),
    ]