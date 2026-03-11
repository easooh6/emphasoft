# Hotel Booking API

REST API для бронирования гостиничных номеров. Django + DRF + PostgreSQL.

## Стек

- Python 3.12
- Django 6.0
- Django REST Framework
- PostgreSQL 16
- Docker / Docker Compose

## Запуск

### 1. Клонировать репозиторий

```bash
git clone <url> && cd emphasoft_tz
```

### 2. Создать `.env`

Скопировать пример и заполнить значения:

```bash
cp .env.example .env
```

```dotenv
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=hotel
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### 3. Запустить через Docker Compose

```bash
docker compose up --build -d
```

### 4. Применить миграции

```bash
docker compose exec web python manage.py migrate
```

### 5. Создать суперпользователя

```bash
docker compose exec web python manage.py createsuperuser
```

### 6. Готово

Приложение доступно по адресу: http://localhost:8000

## API эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| POST | `/api/v1/register/` | Регистрация |
| POST | `/api/v1/login/` | Получение JWT токена |
| POST | `/api/v1/token/refresh/` | Обновление токена |
| GET | `/api/v1/rooms/` | Список номеров |
| GET/POST | `/api/v1/bookings/` | Бронирования |
| DELETE | `/api/v1/bookings/{id}/` | Отмена бронирования |

## Документация API

- Swagger UI: http://localhost:8000/api/docs/swagger/
- ReDoc: http://localhost:8000/api/docs/redoc/

## Тесты

```bash
docker compose exec web python -m pytest
```
