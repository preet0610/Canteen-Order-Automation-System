# Generated by Django 4.0.3 on 2022-04-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation_system', '0003_userext_hall'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delived',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
