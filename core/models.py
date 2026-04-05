from django.db import models
from accounts.models import Shopkeeper
# Create your models here.

class Customer(models.Model):
    shopkeeper = models.ForeignKey(Shopkeeper, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15,unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name
    

class Product(models.Model):
    shopkeeper = models.ForeignKey(Shopkeeper, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    cutomer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    taken_by_name = models.CharField(max_length=100,null=True,blank=True)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction {self.id}" 

class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
class Payment(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.customer_name}-{self.amount}"
        
           