# Generated by Django 2.2.5 on 2021-03-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210224_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('KRW', 'KRW'), ('USD', 'USD')], default='KRW', max_length=3),
        ),
    ]
