from django.db import models

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Receipt(models.Model):
    image = models.ImageField(upload_to='receipts/')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    vendor = models.CharField(max_length=200, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.vendor} - {self.total_amount}"
