# 🎬 django-movie-api API

REST API для управления базой фильмов. Построен на Django REST Framework с JWT-аутентификацией и Swagger документацией.

## 🛠 Стек технологий

- **Python 3.12** + **Django**
- **Django REST Framework**
- **PostgreSQL**
- **JWT** (Simple JWT)
- **Swagger** (drf-yasg)
- **Docker** + **Docker Compose**

## 📦 Возможности

- Регистрация и аутентификация пользователей (JWT)
- CRUD для фильмов, жанров и актёров
- Фильтрация по году и бюджету
- Поиск по названию, актёрам и жанрам
- Сортировка по году и бюджету
- Автодокументация через Swagger UI

## 🚀 Быстрый старт (через Docker)

### 1. Клонируй репозиторий

```bash
git clone git@github.com:Darigaai/django-movie-api.git
cd django-movie-api
```

### 2. Создай `.env` файл

```bash
cp .env.example .env
```

Заполни `.env`:

```env
POSTGRES_DB=mydb
POSTGRES_USER=admin
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
DEBUG=1
SECRET_KEY=your-secret-key
```

### 3. Запусти через Docker Compose

```bash
docker-compose up --build
```

API будет доступен по адресу: `http://localhost:8000`

---

## 📖 Без Docker (локально)

```bash
# Создай виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Установи зависимости
pip install -r requirements.txt

# Применить миграции
python manage.py migrate

# Запустить сервер
python manage.py runserver
```

---

## 🔑 Аутентификация

Проект использует JWT. Все эндпоинты (кроме регистрации) требуют токен в заголовке:

```
Authorization: Bearer <access_token>
```

---

## 📡 Основные эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| POST | `/api/users/register/` | Регистрация |
| POST | `/api/token/` | Получить токены |
| POST | `/api/token/refresh/` | Обновить access токен |
| GET/POST | `/api/movies/` | Список фильмов / создать |
| GET/PUT/DELETE | `/api/movies/{id}/` | Фильм по id |
| GET/POST | `/api/genres/` | Жанры |
| GET/POST | `/api/actors/` | Актёры |

### Фильтрация фильмов

```
GET /api/movies/?year__gte=2000&year__lte=2023
GET /api/movies/?budget__gte=1000000
GET /api/movies/?search=Inception
GET /api/movies/?ordering=-year
```

---

## 📚 Swagger документация

После запуска открой: `http://localhost:8000/swagger/`

---

## 🗂 Структура проекта

```
django-movie-api/
├── core/               # Настройки Django
│   ├── settings.py
│   └── urls.py
├── movie/              # Приложение фильмов
│   ├── models.py       # Genre, Actor, Movie
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── users/              # Приложение пользователей
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env.example
```

---

## 📝 Заполнение тестовыми данными

```bash
python manage.py runscript populate_db
```
