# Generated by Django 4.2 on 2023-05-21 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_profile_activity_level_alter_profile_gender'),
        ('db_app', '0007_alter_meallog_date_shoppingproducts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShoppingProducts',
            new_name='ShoppingProduct',
        ),
        migrations.AlterField(
            model_name='meallog',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 21, 19, 56, 55, 114093, tzinfo=datetime.timezone.utc)),
        ),
    ]
