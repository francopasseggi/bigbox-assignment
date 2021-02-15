from django.contrib import admin

from .models import Box, Activity, Category, Reason

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('pk','name', 'internal_name','price', 'purchase_available')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'internal_name', 'purchase_available')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order', 'description')

@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display  = ('name', 'slug', 'order')