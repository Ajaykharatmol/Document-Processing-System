# Generated by Django 5.1 on 2024-08-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document_Processing', '0006_alter_document_upload_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Upload_Document',
            field=models.FileField(upload_to=''),
        ),
    ]
