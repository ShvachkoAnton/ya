# Generated by Django 3.2.5 on 2021-07-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_remove_profile_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=25, null=True, verbose_name='введите текст'),
        ),
    ]
