# Generated by Django 4.1.1 on 2022-09-19 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_clientimage_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientimage',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clientimage', to='clients.client', verbose_name='Клиент'),
        ),
    ]
