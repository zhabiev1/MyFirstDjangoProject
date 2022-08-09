Create new GIT repository:
1. git init
2. git remote add origin <link>
3. git add .
4. git status
5. create commit 
6. push

Update GIT repository:
1. git add .
2. git status
3. create commit 
4. push

Create Django Project:
1. File -> Open
2. Pycharm projects -> MyDjangoProject
3. Open
4. django-admin startproject <name>
5. Create venv
6. python -m pip install Django

Create and activate venv:
1. python3 -m venv django-env
2. source django-env/bin/activate

Command Django:
1. python manage.py runserver - запуск проекта 
2. python manage.py startapp <name-app> - создать отдельное приложение

Usage of migration:
1. python manage.py migrate 

Creating new migration:
1. python manage.py makemigrations
2. python manage.py migrate 

Create superuser:
1. python manage.py createsuperuser



