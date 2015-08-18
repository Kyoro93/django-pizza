from django.contrib import admin

from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ingredients','price']
    list_display = ['name', 'ingredients', 'price']

admin.site.register(Pizza, PizzaAdmin)
