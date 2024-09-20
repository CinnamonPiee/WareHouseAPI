# FastAPI API для управления складом
Этот проект представляет собой REST API, разработанное с использованием FastAPI для управления товарами, заказами и складскими запасами. Взаимодействие с базой данных осуществляется через асинхронную версию SQLAlchemy 2.0. Весь проект контейнеризован с использованием Docker и Docker Compose.
## Основные возможности
- **Товары**: Добавление, получение, обновление и удаление товаров.
- **Заказы**: Создание заказов, обновление их статуса и проверка наличия товаров.
- **Управление запасами**: Автоматическое обновление запасов при создании заказа.
- **Асинхронный доступ к БД**: Используется SQLAlchemy 2.0 с поддержкой асинхронных операций.
- **Документация API**: Swagger UI для удобного взаимодействия с API.
## Предварительные требования
Перед началом работы убедитесь, что у вас установлены:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
## Инструкция по настройке
### 1. Клонируйте репозиторий
```bash
git clone <url-репозитория>
cd <директория-проекта>
```
### 2. Создайте файл .env на примере файла .env.template
DB_HOST=YOUR_DB_HOST\
DB_PORT=YOUR_DB_PORT\
DB_USER=YOUR_DB_USER\
DB_PASS=YOUR_DB_PASS\
DB_NAME=YOUR_DB_NAME\
TEST_DB_USER=YOUR_TEST_DB_USER\
TEST_DB_PASS=YOUR_TEST_DB_PASS\
TEST_DB_HOST=YOUR_TEST_DB_HOST\
TEST_DB_PORT=YOUR_TEST_DB_PORT\
TEST_DB_NAME=YOUR_TEST_DB_NAME\
### 3. Соберите и запустите Docker контейнеры
```bash
docker-compose up --build
```
Эта команда выполнит следующие действия:
* Соберет образ FastAPI приложения на основе Dockerfile.
* Запустит базу данных PostgreSQL в отдельном контейнере.
* Запустит FastAPI приложение по адресу http://localhost:8000.
### 4. Доступ к документации API
```bash
http://localhost:8000/docs
```
Это откроет интерфейс Swagger UI, где можно протестировать все эндпоинты.
### 5. Миграции
Для управления миграциями базы данных можно использовать Alembic. Вот краткая инструкция:
Инициализируйте Alembic (если не было сделано ранее):
```bash
alembic init alembic
```
Сгенерируйте миграцию:
```bash
alembic revision --autogenerate -m "Initial migration"
```
Примените миграцию:
```bash
alembic upgrade head
```
### 6. Запуск тестов
```bash
pytest
```
### 7. Управление Docker
Остановка контейнеров:
```bash
docker-compose down
```
Пересборка образов без использования кеша:
```bash
docker-compose build --no-cache
```