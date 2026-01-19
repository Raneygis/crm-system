from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task_type', 'priority', 'status', 'assigned_to', 'contact', 'deal', 'due_date', 'completed_at')
    list_filter = ('task_type', 'priority', 'status', 'created_at', 'due_date')
    search_fields = ('title', 'description', 'assigned_to__username', 'contact__first_name', 'contact__last_name')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'due_date'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'task_type')
        }),
        ('Статус и приоритет', {
            'fields': ('priority', 'status')
        }),
        ('Связи', {
            'fields': ('contact', 'deal')
        }),
        ('Исполнители', {
            'fields': ('assigned_to', 'created_by')
        }),
        ('Сроки', {
            'fields': ('due_date', 'completed_at', 'created_at', 'updated_at')
        }),
    )
