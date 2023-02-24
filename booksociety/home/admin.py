from django.contrib import admin
from .models import Category,Products

class CategoryAdmin(admin.ModelAdmin):
    list_display=("name","img")

class ProductsAdmin(admin.ModelAdmin):
    list_display=("pro","name","img","desc","qty","discount","price")


admin.site.register(Category,CategoryAdmin)
admin.site.register(Products,ProductsAdmin)