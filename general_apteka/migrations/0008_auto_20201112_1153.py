# Generated by Django 2.0.6 on 2020-11-12 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_apteka', '0007_auto_20201110_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qr_code',
        ),
        migrations.RemoveField(
            model_name='product',
            name='qr_code_value',
        ),
    ]
