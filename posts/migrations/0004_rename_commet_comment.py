# Generated by Django 4.2.3 on 2023-08-10 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_commet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commet',
            new_name='Comment',
        ),
    ]
