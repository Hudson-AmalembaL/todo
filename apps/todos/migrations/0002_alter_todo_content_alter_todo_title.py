# Generated by Django 4.0.2 on 2022-02-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(verbose_name='Todo Contents'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Todo Title'),
        ),
    ]
