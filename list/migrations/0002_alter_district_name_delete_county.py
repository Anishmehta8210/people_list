# Generated by Django 4.2 on 2023-05-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='County',
        ),
    ]
