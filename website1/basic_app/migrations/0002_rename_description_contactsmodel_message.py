# Generated by Django 4.0.3 on 2022-03-27 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactsmodel',
            old_name='description',
            new_name='message',
        ),
    ]
