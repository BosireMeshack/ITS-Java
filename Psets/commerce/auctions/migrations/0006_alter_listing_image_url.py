# Generated by Django 5.0 on 2024-02-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0005_rename_category_category_category_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="image_url",
            field=models.CharField(max_length=1000),
        ),
    ]
