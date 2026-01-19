from django.db import models
from apps.users.models import CustomUser
from apps.contacts.models import Contact
from apps.deals.models import Deal

class Task(models.Model):
    PRIORITIES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
        ('urgent', 'Срочный'),
    ]
    
    STATUSES = [
        ('todo', 'К выполнению'),
        ('in_progress', 'В работе'),
        ('review', 'На проверке'),
        ('done', 'Выполнено'),
        ('cancelled', 'Отменено'),
    ]
    
    TASK_TYPES = [
        ('call', 'Звонок'),
        ('meeting', 'Встреча'),
        ('email', 'Письмо'),
        ('document', 'Документ'),
        ('other', 'Другое'),
    ]
    
    title = models.CharField('Название задачи', max_length=200)
    description = models.TextField('Описание', blank=True)
    task_type = models.CharField('Тип задачи', max_length=20, choices=TASK_TYPES, default='other')
    priority = models.CharField('Приоритет', max_length=20, choices=PRIORITIES, default='medium')
    status = models.CharField('Статус', max_length=20, choices=STATUSES, default='todo')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks', verbose_name='Исполнитель')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_tasks', verbose_name='Создатель')
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks', verbose_name='Контакт')
    deal = models.ForeignKey(Deal, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks', verbose_name='Сделка')
    due_date = models.DateTimeField('Срок выполнения', blank=True, null=True)
    completed_at = models.DateTimeField('Завершено', blank=True, null=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-due_date', 'priority']
    
    def __str__(self):
        return self.title
