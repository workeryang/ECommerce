# Generated by Django 2.2 on 2020-09-09 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200909_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='is_super',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
