# FastAPI_Pg_Counter_App

## Описание проекта

    Это небольшое FastAPI-приложение в контейнере Docker, которое использует PostgreSQL в качестве базы данных 
    и jinja2 для отображения веб-страницы. 
    Оно иллюстрирует взаимодействие между микросервисами приложения и базой данных.
    Каждый раз при обращении к главной странице /"" и таблице counter_table в базе данных counter_db 
    на главной странице отображается и инкрементируется счетчик counter.  

## Описание функционала

Приложение предоставляет простой веб-интерфейс, где при каждом запросе к главной странице:

    Происходит обращение к таблице в базе данных PostgreSQL.
    Берется значение поля count из созданной таблицы.
    Значение увеличивается на 1.
    Ответ отправляется в виде числа.
    Значение count отображается на главной странице.

## Требования

Перед началом работы убедитесь, что у вас установлены следующие компоненты:
    
    - Docker
    - Docker Compose

## Начало работы

Настройка переменных окружения:

Создайте файл .env в корневом каталоге и установите следующие переменные окружения:
    
    POSTGRESS_DB_USER=counter_user
    POSTGRESS_DB_PASSWORD=TheP@ssw0rD
    POSTGRESS_DB_HOST_PORT=5432
    APP_HOST_PORT=8001

Запуск Docker контейнеров:
docker-compose up -d --build
    -d запускает контейнеры в фоновом режиме.
    --build заставляет Docker Compose пересобирать образы, если есть изменения.

Запуск приложения локально:
poetry run  uvicorn app.main:app --host 0.0.0.0 --port 8001

Перезапуск приложения локально:
    poetry run uvicorn app.main:app --reload

Доступ к FastAPI приложению:

    Откройте http://127.0.0.1:8001 (или порт, указанный в вашем файле .env).

Остановка приложения

Для остановки работающих контейнеров используйте следующую команду:

    docker-compose down

## Примечания

    FastAPI приложение доступно по адресу http://localhost:8001
    PostgreSQL работает на порту 5431
    Убедитесь, что у вашей системы есть необходимые права для выполнения команд Docker.
    Файлы конфигурации намеренно оставлены в проекте и отсутствуют в .gitignore
