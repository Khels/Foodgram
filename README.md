# yamdb_final
![YaMDB workflow](https://github.com/Khels/foodgram-project-react/actions/workflows/main.yml/badge.svg)
### Описание
Сайт Foodgram хранит рецепты от пользователей, которые можно фильтровать по тегам, добавлять в избранное и в список покупок.
### Технологии
- Python3
- Django
- Django Rest Framework
- gunicorn
- Docker
- docker-compose
- Nginx
- Postgres
### Ссылка на сайт
Проект развёрнут на удалённом сервере и доступен по адресу: http://foodgrams.ml
### Начало работы

Пособие по установке Docker: https://docs.docker.com/engine/install/  

И docker-compose: https://docs.docker.com/compose/install/  

Для развёртывания приложения на основе контейнеров Docker нужно перейти в корневую директорию проекта и оттуда выполнить следующую команду:  
```docker-compose up -d --build```  

Чтобы остановить контейнеры достаточно:  
```docker-compose stop```  

А для их полного удаления (с удалением томов):  
```docker-compose down -v```  

Для создания суперпользователя сначала нужно выполнить миграции:  
```docker-compose exec web python3 project/manage.py migrate --no-input```  

И лишь после этого:  
```docker-compose exec web python3 project/manage.py createsuperuser```  

Для создания бэкап-файла БД нужно выполнить:  
```docker-compose exec web python3 project/manage.py dumpdata > [YOUR_DUMP_FILE_NAME].json```  

Для заполнения БД тестовыми данными:  
```docker-compose exec web python3 project/manage.py loaddata fixtures.json```  

### Автор
Khels Kelly
