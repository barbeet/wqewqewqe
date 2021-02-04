# Generated by Django 2.0.6 on 2020-11-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_apteka', '0003_auto_20201109_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateNewOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_product_id', models.CharField(max_length=1000)),
                ('method_of_obtaining', models.CharField(max_length=100)),
                ('payment_method', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('status', models.CharField(default='В процессе', max_length=100)),
            ],
        ),
    ]