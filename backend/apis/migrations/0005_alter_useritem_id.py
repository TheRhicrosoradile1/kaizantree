# Generated by Django 5.0.2 on 2024-02-12 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_useritem_item_useritem_user_alter_item_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useritem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]