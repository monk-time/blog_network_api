# blog_network_api
REST API для [социальной сети блогеров](https://github.com/monk-time/blog_network). Позволяет удаленно управлять публикациями и комментариями, создавать подписки и получать информацию о сообществах.

### Используемые технологии
API написан на Django/DRF, для управления пользователями и аутентификации через JWT-токены используются библиотеки djoser и djangorestframework-simplejwt.

Также см. [альтернативную реализацию API на FastAPI](https://github.com/monk-time/blog_network_fastapi).

### Как запустить проект
1. Клонируйте репозиторий и перейдите в него в командной строке:
    ```bash
    git clone https://github.com/monk-time/blog_network_api.git
    cd blog_network_api
    ```

2. Cоздайте и активируйте виртуальное окружение:
    ```bash
    python3 -m venv venv
    # Для Linux/macOS:
    source venv/bin/activate
    # Для Windows:
    source venv/Scripts/activate
    ```

3. Установите зависимости из файла requirements.txt:
    ```bash
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Выполните миграции и запустите проект:
    ```bash
    python3 manage.py migrate
    python3 manage.py runserver
    ```

### Примеры запросов
- Подробная документация API: `/redoc/` (GET)
- Получить JWT-токен: `api/v1/jwt/create/` (POST)
    ```json
    {
        "username": "string",
        "password": "string"
    }
    ```
- Получить список всех публикаций: `/api/v1/posts/` (GET)
- Создать новую публикацию: `/api/v1/posts/` (POST)
    ```json
    {
        "text": "Новый пост",
        "image": "data:image/png;base64,<...>",
        "group": 1
    }
    ```
- Удалить комментарий к публикации: `/api/v1/posts/{post_id}/comments/{id}/` (DELETE)
- Получить информацию о сообществе: `/api/v1/groups/{id}/` (GET)
- Подписаться на пользователя: `/api/v1/follow/` (POST)
    ```json
    {
        "following": "username"
    }
    ```

### Об авторе
Дмитрий Богорад [@monk-time](https://github.com/monk-time)
