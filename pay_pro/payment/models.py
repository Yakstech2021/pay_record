from django.db import models
from django.urls import reverse



class Payment(models.Model):
    
    payment_name = models.CharField(max_length=100)
    cash_from_bank = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Cash from bank ")
    cash_to_bank = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Cash to bank ")
    revenue_from_counter = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Revenue From Counter")
    remittance_from_counter = models.DecimalField(max_digits=100, decimal_places=2,
                                                  verbose_name="Remittance From Counter")
    deposit_from_counter = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Deposit From Counter")
    revenue = models.DecimalField(max_digits=100,decimal_places=2,verbose_name="revenue", null=True)
    remittance = models.DecimalField(max_digits=100,decimal_places=2,verbose_name="remittance",null=True)
    deposit = models.DecimalField(max_digits=100,decimal_places=2,verbose_name="deposit", null=True)
    def __str__(self):
        return self.payment_name

    def get_absolute_url(self):
        return reverse('payment/detail/<int:id>', args=[self.id])
