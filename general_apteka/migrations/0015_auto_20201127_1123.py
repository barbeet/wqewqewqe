# Generated by Django 2.0.6 on 2020-11-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_apteka', '0014_product_testimony'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='methods_of_application',
        ),
        migrations.RemoveField(
            model_name='product',
            name='testimony',
        ),
        migrations.AddField(
            model_name='product',
            name='application_methods',
            field=models.TextField(default='Информация отсутствует.'),
        ),
        migrations.AddField(
            model_name='product',
            name='characteristics',
            field=models.TextField(default='default.png'),
        ),
        migrations.AddField(
            model_name='product',
            name='composition',
            field=models.TextField(default='Информация отсутствует.'),
        ),
        migrations.AddField(
            model_name='product',
            name='contraindications',
            field=models.TextField(default='Информация отсутствует.'),
        ),
        migrations.AddField(
            model_name='product',
            name='general_description',
            field=models.TextField(default='Информация отсутствует.'),
        ),
        migrations.AddField(
            model_name='product',
            name='indications',
            field=models.TextField(default='Информация отсутствует.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='Информация отсутствует.'),
        ),
    ]
