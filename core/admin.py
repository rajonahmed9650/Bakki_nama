from django.contrib import admin
from .models import Customer,Product,Transaction,TransactionItem,Payment

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(TransactionItem)
admin.site.register(Payment)
