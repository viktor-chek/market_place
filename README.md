<h2 align="center">Сеть электроники (Тестовое задание)</h2> 

`Stack:`

Python 3.10

Django 4.1.7

DRF 3.14.0

Postgresql 15.2

Docker

___
`Описание приложения:`

Веб-приложение с API интерфейсом на Django и админ-панелью. Реализован функционал сети по продаже электроники.
              
Код задокументирован Swagger
___
`Запуск:`

- Клонировать репозиторий
- Установить виртуальное окружение и зависимости из requirements.txt
- Создать и заполнить .env файл по образцу из корня
- Поднять базу в докер: `docker run --name postgres_test -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres`
- Применить миграции: `python manage.py migrate`
- Создать пользователя командой: `python manage.py createsuperuser`
- Запустить сервер: `python manage.py runserver`



