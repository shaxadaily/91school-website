# Generated by Django 4.2.3 on 2023-07-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comments_created_at_alter_news_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='subtitle',
            field=models.TextField(default='Подзаголовок', verbose_name='Подзаголовок'),
        ),
    ]