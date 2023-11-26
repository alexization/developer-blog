# Generated by Django 3.1.3 on 2023-11-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_auto_20231121_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='p_secure',
        ),
        migrations.AlterField(
            model_name='post',
            name='p_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='p_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
