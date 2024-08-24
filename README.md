# Document Service

## Установка и запуск

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/SSkeris/docs_service.git
   
2. Запустите Docker:

    ```bash
    docker-compose up --build

3. Создайте суперпользователя для доступа к Django admin:
    
   ```bash
    docker-compose exec app python manage.py csu

4. Откройте браузер и перейдите по адресу:

http://localhost:8000/admin/

#  Пользовательская модель
Для управления пользователями используйте эндпоинт:

POST /api/users/

Пример запроса:

    {
      "email": "testuser@example.com",
      "password": "password123"
    }
## С подробной документацией по API можно ознакомиться по адресу:

http://localhost:8000/swagger/

# Запуск тестов
Для запуска тестов выполните команду:

    docker-compose exec app python manage.py test