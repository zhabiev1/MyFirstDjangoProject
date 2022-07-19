Представление и маршрутизация(обработка запроса)
представление(view) есть в каждом созданном приложении проекта(views.py)
В этих файлах мы описываем функции(вьюшки) которые будут обрабатывать наши запросы

def index(request):
    return HttpResponse("<h2>Главная страница</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

В данном случае выш мы используем класс HttpResponse
его нужно импортировать с помощью  from django.http import HttpResponse
HttpResponse – предназначен для отправки html страниц на сервер

После создания вью для визуализации результата нам нужно описать URLS
Они описываются в главном приложении проекта в файле urls.py

Для того чтобы описывать новые urls проэкта нуужно использовать лист urlpatterns
И сделать импорт из view  from firstapp import views

Для создания новой юрл в листе urlspatterns используется функция path()
Функция path() принимает два параметра:
1. Ссылка на страницу(если главная страница тогда пустая строка)
2. Вьюшка будет обрабатываться по этой ссылке

urlpatterns = [
    path('admin/', admin.site.urls)
    path('', views.index),  описывает главную страницу сайта
    path('about/', views.about),
    path('contact/', views.contact),
]


После этого мы можем увидеть результат после команды python manage.py runserver


