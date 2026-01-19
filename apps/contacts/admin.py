from django.contrib import admin
from .models import Contact, Company

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company', 'position', 'email', 'phone', 'contact_type', 'created_by', 'created_at')
    list_filter = ('contact_type', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'company', 'position')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'last_name', 'middle_name', 'company', 'position')
        }),
        ('Контактные данные', {
            'fields': ('email', 'phone', 'contact_type')
        }),
        ('Дополнительно', {
            'fields': ('notes', 'created_by', 'created_at', 'updated_at')
        }),
    )

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'kpp', 'industry', 'created_at')
    list_filter = ('industry', 'created_at')
    search_fields = ('name', 'inn', 'kpp', 'address')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'industry')
        }),
        ('Реквизиты', {
            'fields': ('inn', 'kpp', 'address', 'website')
        }),
        ('Дополнительно', {
            'fields': ('created_at', 'updated_at')
        }),
    )
