# Generated by Django 3.1.3 on 2020-11-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20201113_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information_post',
            name='create_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='notice_post',
            name='create_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='result_post',
            name='create_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
