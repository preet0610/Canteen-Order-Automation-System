# Generated by Django 4.0.3 on 2022-03-20 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.IntegerField(null=True)),
                ('item', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(null=True)),
                ('avail', models.BooleanField(null=True)),
                ('isveg', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserExt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField(null=True)),
                ('phone', models.BigIntegerField(null=True)),
                ('isStaff', models.BooleanField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automation_system.menuitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automation_system.userext')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.IntegerField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('dt', models.IntegerField(null=True)),
                ('paymode', models.IntegerField(null=True)),
                ('paystatus', models.IntegerField(null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automation_system.menuitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automation_system.userext')),
            ],
        ),
    ]
