from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'address', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'address')
