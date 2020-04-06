# Django-Cipher-Page

#### Данный web проект написан при помощи фреймворка django и реализует шифр Fernet из модуля cryptography.

Для запуска проекта нужно сначала создать виртуальное python окружение и активировать его
```
pip install virtualenv
python3 -m venv env
# активация среды на Linux
source env/bin/activate
# активация среды на Windows
env\bin\activate.bat
```
далее подгрузить все зависимости, содержащиеся в requirements.txt при помощи команды 
```
pip install -r requirements.txt
```
и запустить файл manage.py из корневой папки при помощи команды
```
python manage.py runserver
```

Программа содержит страницу регистрации для ещё не зарегистрированных пользователей (/register) и страницу авторизации 
для зарегистрированных (/login) (authenticate и login из модуля django.contrib.auth).
После успешного прохождения регистрации/авторизации производиться редирект на страницу с шифром, 
находящегося по ссылке /cipher.

Создание суперпользователя:
```
python manage.py createsuperuser
```

Встроенная админ панель django, находящейся по адресу /admin, позволяет совершать CRUD операции для управления базой данных.

Для построения html страниц использовался шаблонизатор django templates. 