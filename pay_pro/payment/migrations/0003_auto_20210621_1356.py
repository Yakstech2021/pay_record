# Generated by Django 3.2.4 on 2021-06-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_payment_payment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='deposit',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True, verbose_name='deposit'),
        ),
        migrations.AddField(
            model_name='payment',
            name='revenue',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True, verbose_name='remittance'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_name',
            field=models.CharField(max_length=100),
        ),
    ]