from django.db import models

# Create your models here.




class Invoice(models.Model):
	customer = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now=True)
	total_quantity = models.IntegerField(default=0)
	total_amount = models.IntegerField(default=0)
	#transaction = models.ForeignKey(Transaction)
	def __str__(self):
		return str(self.id)


class Transaction(models.Model):
	product = models.CharField(max_length=200)
	quantity = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=20,decimal_places=4)
	line_total = models.DecimalField(max_digits=20,decimal_places=4)
	invoice_id = models.ForeignKey(Invoice,related_name='transactions')
	def __str__(self):
		return self.product +","+ str(self.quantity)
