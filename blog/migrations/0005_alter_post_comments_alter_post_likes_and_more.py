# Generated by Django 4.2.5 on 2023-10-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_user_avatar_alter_user_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="comments",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="post",
            name="views",
            field=models.IntegerField(default=0),
        ),
    ]
