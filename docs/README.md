# Weather docker app

## Описание

Это простое веб-приложение для тестового задания.
Приложение написано на Python с использованием FastAPI и работает с базой данных PostgreSQL.
Весь проект разворачивается через Docker Compose и использует Nginx как reverse proxy.

## Запуск приложения

- Склонировать репозиторий.
  `git clone <репозиторий>`
- Перейти в папку docker.
  `cd docker`
- Выполнить команду:
  `sudo docker compose up --build -d`

## Как проверить работу приложения

Примеры запросов:

- GET /ping

  ```bash
  curl http://localhost/ping
  # Ответ: <h1>PONG</h1>
  ```

- GET /health

  ```bash
  curl http://localhost/health
  # Ответ: {"status": "HEALTHY"}
  ```

- GET /list

  ```bash
  curl http://localhost/list
  # Ответ: HTML со списком городов и температур
  ```

- POST /add

  ```bash
  curl -X POST http://localhost/add -H "Content-Type: application/json" -d '{"city": "Moscow", "temperature": 25}'
  ```

### Проверка подключения к PostgreSQL

```bash
sudo docker compose exec postgres psql -U user -d weatherdb
SELECT * FROM weather;
```
