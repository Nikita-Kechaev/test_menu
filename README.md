# Menu
### Описание проекта
    Тестовое

### Инструкция по развертыванию проекта:

    Клонировать репозиторий и перейти в него в командной строке:

    git clone https://github.com/Nikita-Kechaev/test_menu

        cd test_menu

    Cоздать и активировать виртуальное окружение:

        For Unix: python3 -m venv env
        for Win: python -m venv venv

        For Unix: source env/bin/activate
        for Win: PS: venv/scripts/activate
        OR cmd: /venv/Scripts/activate.bat

        For Unix: python3 -m pip install --upgrade pip
        for Win: python -m pip install --upgrade pip

    Установить зависимости из файла requirements.txt:

        For Unix: pip install -r requirements.txt
        for Win: pip install -r requirements.txt

    Выполнить миграции:
        For Unix: python3 manage.py makemigrations
        For Unix: python3 manage.py migrate
     
    Создать суперпользователя:
        For Unix: python3 manage.py createsuperuser
        
 
    Запустить проект:

        For Unix: python3 manage.py runserver
        for Win: python manage.py runserver

### Системные требования
        Зависимости и необходимые системные требования нах - ся в файле requirements.txt
    
### Расширение проекта
        Не успел решить проблему с активной ссылкой в подменю? Контейнеризация.
    
### Примечание
        Создавая пункт меню необходимо указывать верхний уровень и нижние уровни соответственно. (для верхних уровней - необязательно). 
    

