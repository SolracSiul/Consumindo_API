# Generated by Django 4.0.2 on 2022-02-18 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConsultaAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipspublicados',
            name='ip_query',
            field=models.CharField(max_length=100),
        ),
    ]