# Generated by Django 4.0.3 on 2023-03-15 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_rest', '0005_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='join_date',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='!jc6scJsH25roOQjcnb76cjzb9jRuakpWJ7hUnRaH', max_length=128),
        ),
    ]