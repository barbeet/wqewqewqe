# Generated by Django 2.0.6 on 2020-11-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_apteka', '0013_reviev'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='testimony',
            field=models.TextField(default='new'),
            preserve_default=False,
        ),
    ]
