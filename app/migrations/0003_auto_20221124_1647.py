# Generated by Django 3.2.5 on 2022-11-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employee_jjfdsj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='jjfdsj',
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(default='hello', max_length=100),
        ),
    ]