# Generated by Django 4.2.5 on 2023-10-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categori",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]