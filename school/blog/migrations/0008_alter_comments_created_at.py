# Generated by Django 4.2.3 on 2023-07-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_gallery_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
