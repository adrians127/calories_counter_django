# Generated by Django 4.2 on 2023-04-25 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0003_meallog'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipedetail',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
