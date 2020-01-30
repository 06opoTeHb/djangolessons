Добавляем в models.py, в класс Osintservices в конце строчку 

objects = models.Manager()

Далее пишем в views.py в папке osint

<pre>
from django.shortcuts import render
from .models import Osintservices

def post_list(request):
    posts = Osintservices.objects.all()
    return render(request, 'osint/post/main.html', {'posts': posts})
</pre>

в папке osint в urls.py пишем 

<pre>
from django.urls import path
from . import views
app_name = 'osint'
urlpatterns = [
    path('', views.post_list, name='post_list')
]
</pre>

в папке проекта mysite в urls.py пишем

<pre>
from django.urls import path
from django.urls import include
from django.contrib import admin
urlpatterns = [
path('admin/', admin.site.urls),
path('osint/', include('osint.urls', namespace='osint')),
]
</pre>

Теперь идем снова в папку osint и создаем там папку templates, в ней еще одну папку тоже с именем osint, а в ней файл base.html (лежит в этом репозитории)

Потом рядом с этим файлом создаем подкаталог post и в нем файл main.html (он тоже есть в данном репозитории)

Идем назад в папку приложения osint и создаем в ней папку ststic а в ней подпапку osint а в ней файл main.css (он будет в этом репозитории)

Теперь запускаем в терминале PyCharm

python manage.py runserver

И в браузере открываем 

http://127.0.0.1:8000/osint/
