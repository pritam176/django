from django.contrib import admin

from .models import CatalogueRegister

# Register your models here.

class CatalogueRegisterAdmin(admin.ModelAdmin):
    list_display = ("Name", "Number","EmailD", "CreatedDate",)

admin.site.register(CatalogueRegister,CatalogueRegisterAdmin)