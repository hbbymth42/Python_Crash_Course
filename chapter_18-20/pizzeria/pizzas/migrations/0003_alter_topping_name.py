# Generated by Django 4.2.6 on 2023-10-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_topping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.TextField(),
        ),
    ]
