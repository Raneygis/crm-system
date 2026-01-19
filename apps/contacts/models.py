from django.db import models
from apps.users.models import CustomUser

class Contact(models.Model):
    CONTACT_TYPES = [
        ('client', 'Клиент'),
        ('supplier', 'Поставщик'),
        ('partner', 'Партнер'),
        ('other', 'Другое'),
    ]
    
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100, blank=True)
    middle_name = models.CharField('Отчество', max_length=100, blank=True)
    email = models.EmailField('Email', blank=True)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    company = models.CharField('Компания', max_length=200, blank=True)
    position = models.CharField('Должность', max_length=200, blank=True)
    contact_type = models.CharField('Тип контакта', max_length=20, choices=CONTACT_TYPES, default='client')
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_contacts')
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)
    notes = models.TextField('Заметки', blank=True)
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        return f'{self.last_name} {self.first_name} ({self.company})'
    
    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'.strip()

class Company(models.Model):
    name = models.CharField('Название компании', max_length=200, unique=True)
    inn = models.CharField('ИНН', max_length=12, blank=True)
    kpp = models.CharField('КПП', max_length=9, blank=True)
    address = models.TextField('Адрес', blank=True)
    website = models.URLField('Сайт', blank=True)
    industry = models.CharField('Отрасль', max_length=100, blank=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['name']
    
    def __str__(self):
        return self.name

