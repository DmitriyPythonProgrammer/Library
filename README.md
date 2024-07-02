[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=3000&color=F70000&background=000000&random=false&width=435&lines=Created+by+DmitriyPythonProgrammer)](https://git.io/typing-svg)

# Library on fastapi, aiogram, redis, postgresql with docker, docker-compose and nginx
Данный проект представляет собой представление моих текущих хард-скиллов и умений. Это маленькая платформа, которая реализует принцип библиотеки.

Доступ по API, возможность включение header security токена.

Подключён nginx, конфигурационный файл, с возможностью дальнейшего его наполнения настройками.

Подключен телеграмм-бот, который обращается к API, имеет свою собственную бд Redis для хранения состояний.

Это не конечный продукт, а презентация моих текущих умений.

## Технологии
### Веб-сайт (API)
- FastAPI
- postgresql
- async sqlalchemy
- Pydantic
- PyTest
### Telegram бот
- Aiogram3
- Redis
### Куберы и веб-серверы
- Uvicorn
- Nginx
- Docker
- Docker-compose

## Использование
Скачайте проект и запустите через docker-compose (или docker compose), находясь в каталоге:
```
sudo docker compose up
```
Внимание! убедитесь, что на вашей машине не заняты порты, такими службами как: apache, postgresql, redis.
## Разработка

### Требования
Для установки и запуска проекта, необходим Docker, Docker compose.

### Установка зависимостей
Установка зависимостей проиходит автоматиечски при запуске.

## Тестирование
Тестирование API осуществлялось через PyTest.
