# Generated by Django 2.2.12 on 2020-12-10 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_apteka', '0034_auto_20201210_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general_apteka.ProductCategory'),
        ),
    ]
