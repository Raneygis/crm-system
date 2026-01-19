# CRM System

Корпоративная CRM система с отраслевыми модулями.

## Возможности

- 🔐 Аутентификация и авторизация (JWT)
- 👥 Управление пользователями и профилями
- 📇 Контакты и компании
- 💼 Сделки и воронка продаж
- ✅ Задачи и мероприятия
- 🏢 Мультитенантность
- 📱 REST API

## Технологии

- Python 3.10+
- Django 6.0
- Django REST Framework
- PostgreSQL / SQLite
- JWT аутентификация
- Vue.js 3 (фронтенд в разработке)

## Установка

1. Клонируйте репозиторий:
   \\\ash
   git clone https://github.com/raneygis/crm-system.git
   cd crm-system
   \\\

2. Создайте виртуальное окружение:
   \\\ash
   python -m venv venv
   venv\Scripts\activate  # Windows
   \\\

3. Установите зависимости:
   \\\ash
   pip install -r requirements.txt
   \\\

4. Настройте переменные окружения:
   \\\ash
   cp .env.example .env
   # Отредактируйте .env файл
   \\\

5. Выполните миграции:
   \\\ash
   python manage.py migrate
   \\\

6. Создайте суперпользователя:
   \\\ash
   python manage.py createsuperuser
   \\\

7. Запустите сервер:
   \\\ash
   python manage.py runserver
   \\\

## API Endpoints

- \POST /api/auth/token/\ - Получение JWT токена
- \POST /api/auth/token/refresh/\ - Обновление токена
- \GET /api/auth/users/\ - Список пользователей
- \GET /api/auth/users/me/\ - Текущий пользователь

## Структура проекта

\\\
crm-system/
├── apps/                    # Приложения Django
│   ├── users/              # Пользователи и аутентификация
│   ├── contacts/           # Контакты и компании
│   ├── deals/              # Сделки и воронка продаж
│   └── tasks/              # Задачи и мероприятия
├── config/                 # Конфигурация
│   ├── settings/          # Настройки
│   └── api/               # API маршруты
├── core/                   # Ядро Django
├── templates/              # HTML шаблоны
├── media/                  # Загружаемые файлы
└── requirements.txt        # Зависимости
\\\

## Разработка

Проект тестируется с 5 пилотными клиентами:
1. Образовательный центр
2. Агентство недвижимости
3. IT-компания
4. Нефтегазовое оборудование
5. ЗИП для газовых турбин

## Лицензия

MIT License
