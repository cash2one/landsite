from django.contrib import admin
import models



class  CaseImageInline(admin.TabularInline):
    model = models.CaseImage



class CaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    inlines = [CaseImageInline]
    search_fields = ['name',]


admin.site.register(models.Case, CaseAdmin)

admin.site.register(models.CaseImage)
admin.site.register(models.Category)