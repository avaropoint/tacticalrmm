# Generated by Django 4.2.13 on 2024-06-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0046_alter_urlaction_desc_alter_urlaction_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urlaction",
            name="rest_method",
            field=models.CharField(
                choices=[
                    ("get", "Get"),
                    ("post", "Post"),
                    ("put", "Put"),
                    ("delete", "Delete"),
                    ("patch", "Patch"),
                ],
                default="post",
                max_length=10,
            ),
        ),
    ]
