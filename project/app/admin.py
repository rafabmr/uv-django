from django.contrib import admin
from .models import Cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id","nombre", "telefono", "correo")
    list_display_links = ("nombre",)
    search_fields = ("nombre",)


admin.site.register(Cliente, ClienteAdmin)