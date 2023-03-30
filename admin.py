from django.contrib import admin
from .models import DefindedState, Message

# Register your models here.
class DefinedStateAdmin(admin.ModelAdmin):
    list_display = ('name','moisture')
admin.site.register(DefindedState, DefinedStateAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('date','message')
admin.site.register(Message, MessageAdmin)