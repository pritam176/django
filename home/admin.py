from django.contrib import admin

from .models import CatalogueRegister
from .models import CatalogueDocuments

# Register your models here.

class CatalogueRegisterAdmin(admin.ModelAdmin):
    list_display = ("Name", "Number","EmailD", "CreatedDate")
class CatalogueDocumentsAdmin(admin.ModelAdmin):
    list_display = ("docName","docType",  "CreatedDate","isActive")

admin.site.register(CatalogueRegister,CatalogueRegisterAdmin)
admin.site.register(CatalogueDocuments,CatalogueDocumentsAdmin)