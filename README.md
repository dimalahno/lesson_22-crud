# Интернет-магазин (Django)

## Описание проекта
Простой интернет-магазин на Django, который отображает список товаров и детальную информацию о каждом из них.

## Функционал
- Отображение списка товаров
- Просмотр детальной информации о товаре
- Админ-панель для управления товарами
- Загрузка изображений товаров
- Тестирование с `pytest`

## Установка и запуск

### 1. Клонирование репозитория
```sh
git clone https://github.com/yourusername/eshop.git
cd eshop
```

### 2. Создание виртуального окружения
```sh
python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate  # Для Windows
```

### 3. Установка зависимостей
```sh
pip install -r requirements.txt
```

### 4. Настройка базы данных
Примените миграции:
```sh
python manage.py migrate
```

### 5. Создание суперпользователя
```sh
python manage.py createsuperuser
```

### 6. Запуск сервера
```sh
python manage.py runserver
```

### 7. Доступ к админке
Перейдите в браузере: `http://127.0.0.1:8000/admin/`

## Тестирование
Запуск тестов:
```sh
pytest
```

## Структура проекта
```
/eshop/          # Корень проекта
    /eshop/      # Настройки Django
    /products/   # Приложение товаров
    /static/     # Статические файлы
    /templates/  # Шаблоны
    manage.py
    pytest.ini
    requirements.txt
    README.md
```

## Стек технологий
- Python 3.11+
- Django 4+

## Лицензия
MIT License

