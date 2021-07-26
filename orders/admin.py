from django.contrib import admin

from .models import Order, Item


class ItemAdmin(admin.TabularInline):
    model = Item
    # exclude = ('prize')
    # extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('owner', 'status', 'finished', 'total_prize')
    date_hierarhy = 'created'
    empty_value_display = 'пусто'
    inlines = [ItemAdmin, ]
