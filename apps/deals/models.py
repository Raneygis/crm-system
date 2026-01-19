from django.db import models
from apps.users.models import CustomUser
from apps.contacts.models import Contact, Company

class Deal(models.Model):
    STAGES = [
        ('lead', 'Лид'),
        ('contact', 'Контакт'),
        ('proposal', 'Предложение'),
        ('negotiation', 'Переговоры'),
        ('contract', 'Договор'),
        ('won', 'Успех'),
        ('lost', 'Потеря'),
    ]
    
    title = models.CharField('Название сделки', max_length=200)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True, related_name='deals', verbose_name='Контакт')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name='deals', verbose_name='Компания')
    stage = models.CharField('Стадия', max_length=20, choices=STAGES, default='lead')
    amount = models.DecimalField('Сумма', max_digits=12, decimal_places=2, blank=True, null=True)
    currency = models.CharField('Валюта', max_length=3, default='RUB')
    probability = models.IntegerField('Вероятность', default=0)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='deals', verbose_name='Ответственный')
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    deadline = models.DateField('Дедлайн', blank=True, null=True)
    description = models.TextField('Описание', blank=True)
    
    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.title} ({self.get_stage_display()})'
