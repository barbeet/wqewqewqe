# Generated by Django 3.1.5 on 2021-01-26 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_apteka', '0048_productcatalog'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='catalog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='general_apteka.productcatalog'),
        ),
    ]
