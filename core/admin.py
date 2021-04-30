from django.contrib import admin
from core.models import *

# Register your models here.


@admin.register(CSVFiles)
class AdminCSVFiles(admin.ModelAdmin):
    list_display = ("csv_file", "time")


@admin.register(Deals)
class AdminDeals(admin.ModelAdmin):
    list_display = ("customer", "item", "total", "quantity", "date")
    list_per_page = 25
    search_fields = ("customer", "total", "quantity")
