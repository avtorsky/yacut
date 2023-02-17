# Сервис сокращения ссылок на Flask

[Описание](#описание) /
[Развернуть локально](#развернуть-локально) /
[Unit-тестирование](#unit-тестирование) /
[Healthcheck](#healthcheck) /
[История изменений](#история-изменений) /
[Автор](#автор)

## Описание

[YaCut](https://github.com/avtorsky/yacut): веб-интерфейс и API сервиса для сокращения ссылок

## Развернуть локально

Склонировать проект, создать виртуальное окружение и проинициализировать зависимости:

```bash
git clone https://github.com/avtorsky/yacut.git
cd yacut
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Проинициализировать БД, выполнить миграции и запустить сервис:

```bash
flask shell
>>> from yacut import db
>>> db.create_all()
>>> exit()
flask db init
flask run
```

## Unit-тестирование

Тесты запускаются из корневой директории ```./```

```bash
source venv/bin/activate
pytest
```

## Healthcheck

Swagger-cпецификации методов API: [openapi.yml](https://github.com/avtorsky/yacut/blob/master/openapi.yml)
Проверка эндпойнтов сервиса:

```bash
curl -X POST http://localhost:5000/api/id/ \
    -H 'Content-Type: application/json' \
    -d '{"url": "https://yatube.avtorskydeployed.online/", "custom_id": "42"}'

{"short_link": "http://localhost:5000/42", "url": "https://yatube.avtorskydeployed.online/"}
```

```bash
curl -sI -X GET -L http://localhost:5000/42

HTTP/1.1 307 Temporary Redirect
Content-Type: text/html; charset=utf-8
Location: https://yatube.avtorskydeployed.online/
```

## История изменений

Release 20230217:
* feat(./yacut/): структурированы компоненты, подготовлен API, выполнена проверка мигратора
* doc(./README.md): подготовлены спецификации

## Автор

[@avtorsky](https://github.com/avtorsky)
