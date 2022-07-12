project - совокупность многих приложений.
Приложения (app) - отдельная часть проэкта

В главном приложении проекта по стандарту создаётся файл settings.py,в котором хранятся все настройки проекта.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS – отдельные приложения, которые использует проект

Для добавления нового приложения в проект:
1.python manage.py startapp <name-app>
2.зарегистрировать приложение в settings.py(INSTALLED_APPS)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstapp',
]
