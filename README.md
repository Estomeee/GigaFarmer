# MooBot
Проект создан в рамках хакатона от МФТИ 'PHYSTECH GIGACHAT CHALlENGE'

MooBot - Консультационный чат-бот по вопросам животноводства, рационам кормления и управлению фермой.
На основе генеративного чат-бота с искусственным интеллектом Gigachat от Сбера. 

Для запуска проекта:
1) Клонируйте репозиторий: git clone
2) Создайте файл .env на уровне с docker-compose.yml
   В файле должно быть следующее:
   DB_HOST = db
   DB_PORT = 5432
   DB_NAME = postgres
   DB_USER = postgres
   DB_PASS = postgres

   Можно не иенять вышеуказанные параметры. При их изменении, внесите изменения соответсвенно в docker-compose в сервисе db. 
  
   TG_TOKEN = токен для подключения к боту
   GIGA_TOKEN = токен для подключения к GigaChat
4) Соберите docker-compose: docker-compose build
5) Поднимите docker-compose: docker-compose up 
