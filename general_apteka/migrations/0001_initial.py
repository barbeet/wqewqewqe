# Generated by Django 2.0.6 on 2020-11-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasketProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=100)),
                ('setting_product', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product_done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField()),
                ('qr_code', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('qr_code_value', models.CharField(max_length=500)),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.CreateModel(
            name='QrCodeSave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
