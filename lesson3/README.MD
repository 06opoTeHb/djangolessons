python manage.py createsuperuser

Ввести логин и пароль админа

Запустить сервер

python manage.py runserver

Войти в админку http://127.0.0.1:8000/admin/

Добавить в admin.py в папке osint

from .models import Category
admin.site.register(Category)

from .models import Osintservices
admin.site.register(Osintservices)

Поменять язык в settings.py на 'ru'

Обновить страничку, добавить несколько записей в категории, и в OSINT сервисы

