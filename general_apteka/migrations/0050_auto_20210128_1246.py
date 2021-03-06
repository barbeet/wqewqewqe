# Generated by Django 3.1.5 on 2021-01-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_apteka', '0049_productcategory_catalog'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=200, verbose_name='Телефон')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('success', models.BooleanField(default=False, verbose_name='Обработано ДА/НЕТ')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Заявка на обратный звонок',
            },
        ),
        migrations.AlterModelOptions(
            name='productdescription',
            options={'verbose_name': 'Доп описание товара', 'verbose_name_plural': 'Доп описание товара'},
        ),
    ]
