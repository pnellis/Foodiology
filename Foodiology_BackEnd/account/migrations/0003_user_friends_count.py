# Generated by Django 5.0.2 on 2024-03-25 21:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_user_friends_friendshiprequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="friends_count",
            field=models.IntegerField(default=0),
        ),
    ]
