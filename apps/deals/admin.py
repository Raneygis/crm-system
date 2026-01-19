from django.contrib import admin
from .models import Deal

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact', 'company', 'stage', 'amount', 'probability', 'owner', 'deadline', 'created_at')
    list_filter = ('stage', 'currency', 'created_at', 'deadline')
    search_fields = ('title', 'description', 'contact__first_name', 'contact__last_name', 'company__name')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'contact', 'company', 'description')
        }),
        ('Финансы', {
            'fields': ('amount', 'currency')
        }),
        ('Прогресс', {
            'fields': ('stage', 'probability', 'deadline')
        }),
        ('Ответственные', {
            'fields': ('owner',)
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at')
        }),
    )
