# Generated by Django 2.2.5 on 2021-03-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210301_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('KRW', 'KRW'), ('USD', 'USD')], default='KRW', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male'), ('other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('kr', 'Korean'), ('en', 'English')], default='kr', max_length=2),
        ),
    ]
