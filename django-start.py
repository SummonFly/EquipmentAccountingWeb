import os
import subprocess
import sys

project_name = "Equipment_accounting_system"
app_name = "www"


def install_django():
    print("\n>Устанавливаю Django...")
    try:
        subprocess.run(f"pip install django", shell=False)
    except Exception as e:
        print(f'>>>Не удалось установить Django по причине {e}')
        exit()
    print('>Установил')


def create_django_project(project_name):
    print(f'\n\n>Создаю проект {os.curdir}/{project_name}...')
    try:
        subprocess.run(['django-admin', 'startproject', project_name])
    except Exception as e:
        print(f'>>>Не удалось проект по причине {e}')
        exit()


def create_django_app(project_name, app_name):
    print(f">Создаю приложение  '{app_name}' '{os.curdir}/{project_name}/{app_name}'...")
    os.chdir(project_name)
    subprocess.run(['py', 'manage.py', 'startapp', app_name])


def create_url_and_views():
    os.chdir(project_name)
    url = open("urls.py", "w+")
    url.write(""
              "from django.contrib import admin"
              "\nfrom django.urls import path, include"
              "\n"
              "\nurlpatterns = ["
              "\n    path('admin/', admin.site.urls),"
              f"\n    path('', include('{app_name}.urls'))"
              "\n]")
    url.close()
    print(f'>В {project_name} вношу изменения\n -urls.py ')

    with open('settings.py', 'r') as file:
        lines = file.readlines()

    for index, line in enumerate(lines):
        if line.strip().startswith('INSTALLED_APPS'):
            while not lines[index].strip().endswith(']'):
                index += 1
            lines.insert(index, f"    '{app_name}',\n")
            break
    print(' -settings.py')

    with open('settings.py', 'w') as file:
        file.writelines(lines)

    os.chdir(f"../{app_name}")
    url = open("urls.py", "w+")
    url.write(""
              "from django.urls import path"
              "\nfrom .views import *"
              "\n"
              "\nurlpatterns = ["
              "\n    path('', index, name='index'),"
              "\n]")
    url.close()
    print(f'>В {app_name} внес изменения\n -urls.py ')

    views = open("views.py", "w+")
    views.write('from django.shortcuts import render'
                '\n'
                '\n'
                '\n# Create your views here.'
                '\ndef index(request):'
                '\n    return render(request, \'index.html\')')
    views.close()
    print(' -views.py ')


def create_templates_and_index():
    os.mkdir("templates")
    os.chdir('templates')
    temp = open("index.html", "w+")
    temp.write('<!DOCTYPE html>'
               '\n<html lang="ru">'
               '\n<head>'
               '\n    <meta charset="UTF-8">'
               '\n    <title>Hello!</title>'
               '\n</head>'
               '\n<body>'
               '\n    <H1>Hello World</H1>'
               '\n</body>'
               '\n</html>')
    temp.close()
    print(" -templates\\\n   -index.html")


if __name__ == "__main__":
    print('Привет! Я помогу тебе все настроить\nДля начала, давай назовем проект')
    project_name = input('>')
    print('')
    print(f'{project_name}! Звучит не плохо, теперь давай назовем твое приложение')
    app_name = input('>')
    print(f'{project_name}/{app_name} ЗДОРОВО! Начинаю свою работу!')

    install_django()
    create_django_project(project_name)
    create_django_app(project_name, app_name)
    create_url_and_views()
    create_templates_and_index()
    print(f'Все необходимое сделано!\nВыполните команду "cd {project_name}" и "py .\\manage.py runserver"\n\n')