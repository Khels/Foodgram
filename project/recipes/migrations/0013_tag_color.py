# Generated by Django 3.2.4 on 2021-06-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_auto_20210618_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(default='blue', max_length=50, verbose_name='Цвет тега'),
            preserve_default=False,
        ),
    ]
