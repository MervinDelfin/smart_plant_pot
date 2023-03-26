from django.contrib import admin
from .models import DefindedState

# Register your models here.
class DefinedStateAdmin(admin.ModelAdmin):
    list_display = ('name','moisture')
admin.site.register(DefindedState, DefinedStateAdmin)