# Generated by Django 2.1.12 on 2020-12-22 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_apteka', '0041_auto_20201222_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrollBarDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('img', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
                ('href_button', models.CharField(blank=True, max_length=1000, verbose_name='Ссылка кнопки')),
                ('background_color', models.CharField(max_length=200, verbose_name='Цвет заднего фона')),
                ('title_color', models.CharField(max_length=200, verbose_name='Цвет заголовка')),
                ('text_color', models.CharField(max_length=200, verbose_name='Цвет текста ')),
                ('image_background', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение занего фона НЕ обязательно')),
            ],
            options={
                'verbose_name': 'Скролбар cтраница со скидками',
                'verbose_name_plural': 'Скролбар cтраница со скидками',
            },
        ),
    ]
