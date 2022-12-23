# Foodgram - учебный проект.

## На базе фреймворков Django и React реализована мини социальная сеть,**
### **где пользователи могут:**
### ***- размещать рецепты,***
### ***- смотреть рецепты других пользователей,***
### ***- добавлять рецепты и ингредиенты в список покупок,***
### ***- подписываться на публикации понравившихся авторов.***

## >Сервис размещен на VPS сервере и доступен по адресу:
### >http://aaayyy.ru/recipes

## **Технологии:**

### ***Django***
### ***DRF***
### ***Python***
### ***Docker***

## Запуск проекта:

### Клонируйте проект и задайте настройки, для этого:

#### Подключитесь к своему серверу
ssh <server user>@<server IP>
Например: ssh root@00.000.00.00

#### Клонируйте проект на сервер:
git clone git@github.com:RuslGL/foodgram-project-react.git

#### Подготовьте дополнительные данные (.env и nginx.conf):

##### Скопируйте в директорию проекта infra/ файл nginx.conf 
(он есть в репозитории, но на сервер его нужно перенести в ручном режиме)

##### В файле nginx.conf в строке server_name укажите данные ip вашего сервера.

##### Создайте в директории проекта infra/ файл .env и наполните его следующими данными
DEBUG=False
SECRET_KEY=<Длинная строка с латинскими буквами, цифрами и символами>

DB_ENGINE='django.db.backends.postgresql'
DB_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD=<Ваш пароль>
DB_HOST='db'
DB_PORT=5432

#### Подготовьте сервер для работы с проектом:

##### Установите docker и docker-compose:
sudo apt install docker.io 
sudo apt install docker-compose

##### Соберите контейнерs:

sudo docker-compose up -d --build

##### Выполните миграции
sudo docker-compose exec backend python manage.py makemigrations
sudo docker-compose exec backend python manage.py migrate

##### Создайте суперюзера:
sudo docker-compose exec backend python manage.py createsuperuser

##### Cоберите статику
sudo docker-compose exec backend python manage.py collectstatic --no-input

##### Можно работать с преподготовленными ингредиентами, для этого нужно их загрузить командой:

sudo docker-compose exec backend python manage.py import_ingredients_json --path 'recepies/data/ingredients.json'

