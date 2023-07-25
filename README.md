# blog_network_api
API для социальной сети блогеров. Позволяет удаленно управлять публикациями и комментариями, создавать подписки и получать информацию о сообществах.

### Используемые технологии
API реализован на Django/DRF, для управления пользователями и аутентификации используются библиотеки djoser и djangorestframework-simplejwt.

### Как запустить проект
1. Клонировать репозиторий и перейти в него в командной строке:
    ```bash
    git clone https://github.com/monk-time/blog_network_api.git
    cd blog_network_api
    ```

2. Cоздать и активировать виртуальное окружение:
    ```bash
    python3 -m venv venv
    ```

    * Если у вас Linux/macOS

        ```
        source venv/bin/activate
        ```

    * Если у вас windows

        ```
        source venv/Scripts/activate
        ```

3. Установить зависимости из файла requirements.txt:
    ```bash
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Выполнить миграции и запустить проект:
    ```bash
    python3 manage.py migrate
    python3 manage.py runserver
    ```

### Примеры запросов
- Подробная документация API: `/redoc/` (GET)\
- Получить список всех публикаций: `/api/v1/posts/` (GET)\
- Создать новую публикацию: `/api/v1/posts/` (POST)
    ```json
    {
        "text": "Новый пост",
        "image": "data:image/png;base64,<...>",
        "group": 1
    }
    ```
- Удалить комментарий к публикации: `/api/v1/posts/{post_id}/comments/{id}/` (DELETE)\
- Получить информацию о сообществе: `/api/v1/groups/{id}/` (GET)\
- Подписаться на пользователя: `/api/v1/follow/` (POST)
    ```json
    {
        "following": "username"
    }
    ```

### Об авторе
Дмитрий Богорад [@monk-time](https://github.com/monk-time)
