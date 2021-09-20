# Generated by Django 3.2.7 on 2021-09-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210919_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cataloguedocuments',
            name='docType',
            field=models.CharField(choices=[('E', 'E-Catalogue'), ('T', 'Tech. Spec.'), ('C', 'Certificate')], max_length=100),
        ),
    ]