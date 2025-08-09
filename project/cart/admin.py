from django.contrib import admin
from .models import *

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)



