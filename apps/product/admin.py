from django.contrib import admin
import models



class ProductImageInline(admin.TabularInline):
    model = models.ProductImage



class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    inlines = [ProductImageInline]
    search_fields = ['name',]


admin.site.register(models.Product, ProductAdmin)

admin.site.register(models.ProductImage)
admin.site.register(models.Category)
admin.site.register(models.IndexProduct)
