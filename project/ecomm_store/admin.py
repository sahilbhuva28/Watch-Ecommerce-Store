from django.contrib import admin
from django.contrib import messages
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        """ Prevent deletion of categories with associated products. """
        if obj and obj.product_set.exists():
            messages.error(request, f"Cannot delete category '{obj.name}' because it has products.")
            return False
        return True

    def delete_model(self, request, obj):
        """ Override delete function to prevent deletion when products exist. """
        if obj.product_set.exists():
            messages.error(request, f"Cannot delete category '{obj.name}' because it has products.")
        else:
            super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        """ Prevent bulk deletion of categories with products. """
        for obj in queryset:
            if obj.product_set.exists():
                messages.error(request, f"Cannot delete category '{obj.name}' because it has products.")
            else:
                obj.delete()
                messages.success(request, f"Category '{obj.name}' deleted successfully.")

    list_display = ['name', 'category_type', 'description']  # Display category_type in the admin list
    list_filter = ['category_type']  # Add filter by category_type in the admin interface
    search_fields = ['name']  # Add search functionality by category name

class SliderAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')  # Display product and image
    search_fields = ('product__name',)  # Allow searching by product name
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Slider, SliderAdmin)
