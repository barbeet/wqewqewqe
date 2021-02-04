# Generated by Django 3.1.5 on 2021-01-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_apteka', '0046_articles_title_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='title_color',
        ),
        migrations.AddField(
            model_name='articles',
            name='href',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Ссылка кнопки'),
        ),
    ]