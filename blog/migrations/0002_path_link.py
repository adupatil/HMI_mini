# Generated by Django 3.0.5 on 2021-05-07 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='path',
            name='link',
            field=models.TextField(default=''),
        ),
    ]
