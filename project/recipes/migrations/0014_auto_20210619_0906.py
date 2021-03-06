# Generated by Django 3.2.4 on 2021-06-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_tag_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name', 'slug'], 'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='breakfast', max_length=200, verbose_name='Тег (англ.)'),
            preserve_default=False,
        ),
    ]
