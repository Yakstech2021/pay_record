# Generated by Django 3.2.4 on 2021-06-18 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_name', models.CharField(max_length=100)),
                ('cash_from_bank', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Cash from bank ')),
                ('cash_to_bank', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Cash to bank ')),
                ('revenue_from_counter', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Revenue From Counter')),
                ('remittance_from_counter', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Remittance From Counter')),
                ('deposit_from_counter', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Deposit From Counter')),
            ],
        ),
    ]
