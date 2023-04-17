# api_final_yatube
API для социальной сети блогеров Yatube. Позволяет удаленно управлять публикациями и комментариями, создавать подписки и получать информацию о сообществах.

### Используемые технологии
API реализован на Django/DRF, для управления пользователями и аутентификации используются библиотеки djoser и djangorestframework-simplejwt.

### Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/monk-time/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/Scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов
Подробная документация API: `/redoc/` (GET)\
Получить список всех публикаций: `/api/v1/posts/` (GET)\
Создать новую публикацию: `/api/v1/posts/` (POST)
```json
{
    "text": "Новый пост",
    "image": "data:image/png;base64,<...>",
    "group": 1
}
```
Удалить комментарий к публикации: `/api/v1/posts/{post_id}/comments/{id}/` (DELETE)\
Получить информацию о сообществе: `/api/v1/groups/{id}/` (GET)\
Подписаться на пользователя: `/api/v1/follow/` (POST)
```json
{
    "following": "username"
}
```

### Об авторе
Дмитрий Богорад [@monk-time](https://github.com/monk-time). Проект выполнен в рамках курса "Яндекс Практикум" по специальности "Python backend-разработчик".
