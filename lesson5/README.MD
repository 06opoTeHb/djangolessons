Добавим в views.py в папке osint

<pre>from .models import Category</pre>

далее в этом же файле создадим функцию для показа осинт-сервисов с фильтрацией по категориям

<pre>
def post_category(request, url):
    posts = Osintservices.objects.filter(category__url=url)
    menu = Category.objects.all()
    return render(request, 'osint/post/main.html', {'posts': posts, 'menu': menu})
</pre>

файл urls.py в папке osint должен стать таким

<pre>
from django.urls import path
from . import views
app_name = 'osint'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:url>/', views.post_category, name='post_category')
]
</pre>

В файле models.py в класс Category, в конце добавим строчку

<pre>objects = models.Manager()</pre>

Изменим файлы шаблонов и css (измененные файлы лежат на гитхабе в этом каталоге)
