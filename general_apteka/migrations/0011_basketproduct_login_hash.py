# Generated by Django 2.0.6 on 2020-11-23 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_apteka', '0010_product_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketproduct',
            name='login_hash',
            field=models.CharField(default='sadklakfjkldjfioenfoiwnefioewfneoifneoifwniwe', max_length=100),
            preserve_default=False,
        ),
    ]