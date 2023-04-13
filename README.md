# api_final
Проект api_final_yatube является API сервисом для разработанной ранее минисоцсети "Yatube". В этом проекте пользователи с помощью апи запросов могут добавлять/получать посты, комментарии к этим постам, группы, а также подписываться друг на друга. Данный проект является продолжением предыдущего "api_yatube",  в новый проект добавлена модель подписки Follow. К ней описан эндпоинт и вьюсет. Также к проекту подключена пагинация.
# Используемые технологии
+ Python 3.9.10
+ Django REST Framework
+ Postman
+ SQLite3
+ Simple-JWT
# Как запустить проект
`git clone git@github.com:Wandering-npc/api_final_yatube.git`  
`python3 -m venv env`  
`source env/bin/activate`  
`python3 -m pip install --upgrade pip`  
`pip install -r requirements.txt`  
`python3 manage.py migrate`  
`python3 manage.py runserver`  
Документация к API проекта Yatube доступна по адресу http://127.0.0.1:8000/redoc/
# Примеры запросов
Пример POST-запроса с токеном пользователя на добавление нового поста. POST .../api/v1/posts/  
```
{
    "text": "Я мид не проигрываю, а зачастую даже выигрываю"
}
```
Ответ  
```
{
    "id": 1,  
    "author": "Danilo",  
    "text": "Я мид не проигрываю, а зачастую даже выигрываю",  
    "pub_date": "2023-04-13T08:07:08.631429Z",  
    "image": null,  
    "group": null  
}
```
Пример Post-запроса с подпиской на автора к /api/v1/follow/  
```
{
    "user": "Danilo",
    "following": "DANILO"
}
```
Ответ  
```
{
    "id": 1,
    "user": "Danilo",
    "following": "DANILO"
}
```
