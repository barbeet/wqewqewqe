# Generated by Django 2.2.12 on 2020-12-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20201210_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcodesave',
            name='id_product',
            field=models.CharField(default=1, max_length=200, verbose_name='ID продукта'),
            preserve_default=False,
        ),
    ]
