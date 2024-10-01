from django.contrib import admin

# Register your models here.
from .models import Crop  # Ensure to import your Crop model
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'expected_yield')  # Customize the list view
    search_fields = ('name',)  # Enable search functionality

# Register your models here
admin.site.register(Crop)