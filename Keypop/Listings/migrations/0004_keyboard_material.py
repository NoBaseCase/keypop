# Generated by Django 3.2.3 on 2021-05-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listings', '0003_rename_rgb_keyboard_rgb'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyboard',
            name='material',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]