# Generated by Django 5.0.7 on 2024-07-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_student_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excelfileupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(upload_to='excel')),
            ],
        ),
    ]
