# Generated by Django 2.0.6 on 2020-11-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_createneworder'),
    ]

    operations = [
        migrations.AddField(
            model_name='createneworder',
            name='user',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
