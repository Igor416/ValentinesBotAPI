# Generated by Django 4.1.1 on 2023-02-06 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='image',
            new_name='photo',
        ),
    ]
