# Generated by Django 3.2.3 on 2021-05-19 08:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='text',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]