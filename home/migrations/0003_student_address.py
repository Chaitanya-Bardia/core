# Generated by Django 5.0.7 on 2024-07-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default='madurai', max_length=100),
            preserve_default=False,
        ),
    ]
