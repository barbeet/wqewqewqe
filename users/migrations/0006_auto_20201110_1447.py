# Generated by Django 2.0.6 on 2020-11-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_createneworder_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createneworder',
            old_name='all_product_id',
            new_name='all_product_id_and_count',
        ),
        migrations.AddField(
            model_name='createneworder',
            name='sum_all',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
    ]
