from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.paginator import Paginator

import csv


def index(request):
    """Функция обработки адреса и перевод пользователя \

        на страницу /bus_stations.

    """
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    """Функция обработки и вывода на страницу \

        списка автобусных станций, с пагинацией постранично.

    """
    with open('../pagination/data-398-2018-08-30.csv', 'r') as csvfile:
        # открываем файл с расширением "csv",
        # для чтения" и передачи его в шаблон index.html
        reader = csv.DictReader(csvfile)
        bus_stations = list(reader)

    paginator = Paginator(bus_stations, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
    }

    return render(request, 'stations/index.html', context)
