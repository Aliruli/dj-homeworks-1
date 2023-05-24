from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
import datetime


def home(request):
    """Функция обработки адресов и вывода в шаблон, списка ссылок."""
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def current_time(request):
    """Функция обработки и вывода на страницу текущего времени."""
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir(request):
    """Функция обработки и вывода на страницу, списка файлов из дирректории."""
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    files = os.listdir('.')
    files_list = '<br>'.join(files)
    return HttpResponse(files_list)
