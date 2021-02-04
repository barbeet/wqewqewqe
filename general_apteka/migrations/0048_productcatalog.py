# Generated by Django 3.1.5 on 2021-01-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_apteka', '0047_auto_20210125_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog', models.CharField(max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталог',
            },
        ),
    ]