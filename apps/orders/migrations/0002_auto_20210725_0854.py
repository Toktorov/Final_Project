# Generated by Django 2.2.6 on 2021-07-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='arrival_date',
            field=models.DateTimeField(verbose_name='Дата заезда:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='departure_date',
            field=models.DateTimeField(verbose_name='Дата отъезда:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='fatherland',
            field=models.CharField(max_length=50, verbose_name='Отечество:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='surname',
            field=models.CharField(max_length=50, verbose_name='Фамилия:'),
        ),
    ]