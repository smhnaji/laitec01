# Generated by Django 4.0.4 on 2022-05-02 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parent_type',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='parent_id',
            new_name='object_id',
        ),
    ]