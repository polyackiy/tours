from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from django.http import HttpResponse
import logging

import tours.data as data


# View for main page
# TODO: доработать вывод 6 случайных туров
def main_view(request):
    return render(request, "index.html", {
        'subtitle': data.subtitle,
        'description': data.description,
        'tours': data.tours,
    })


# View for page by departure
def departure_view(request, departure):
    return render(request, "tours/departure.html", {
        'title': data.title,
        'subtitle': data.subtitle,
        'description': data.description,
        'departures': data.departures,
        'tours': data.tours,
    })


# View for tours
def tour_view(request, id):
    if id not in data.tours:
        raise Http404

    tour = data.tours.get(id)
    return render(request, "tours/tour.html", {
        'tour': tour,
        'stars': range(int(tour['stars'])),
        'departure': data.departures.get(tour['departure'])
    })


def custom_handler404(request, exception):
    logging.warning(f'Non-existent tour was requested {exception}')
    return HttpResponseNotFound('Кажется такая страница не существует :(')


def custom_handler500(request):
    return HttpResponse('Что-то не так. \nКоманда обученных обезьян была отправлена, чтобы разобраться.', status=500)
