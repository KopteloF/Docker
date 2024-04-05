from django.contrib import admin

# Register your models here.
from logistic.models import Product, StockProduct, Stock


admin.site.register(Product)
admin.site.register(StockProduct)
admin.site.register(Stock)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'description']
#
#
# @admin.register(StockProduct)
# class StockProductAdmin(admin.ModelAdmin):
#     list_display = ['stock', 'product', 'quantity', 'price']
#
#
# @admin.register(Stock)
# class StockAdmin(admin.ModelAdmin):
#     list_display = ['address', 'products']
