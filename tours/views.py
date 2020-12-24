import logging
import random

from django.http import HttpResponse
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render

import tours.data as data


# View for main page
def main_view(request):
    random_list = {}                    # create 6 random tours for main page
    while len(random_list) < 6:
        n = random.randint(1, 16)
        if n not in random_list:
            random_list[n] = data.tours[n]

    return render(request, "index.html", {
        'subtitle': data.subtitle,
        'description': data.description,
        'random_list': random_list,
    })


# View for page by departure
def departure_view(request, departure):
    n_tours, min_price, max_price, min_nights, max_nights = (0, 0, 0, 0, 0)
    tours = {}
    for tour_id, tour in data.tours.items():
        if tour['departure'] == departure:
            n_tours += 1
            tours[tour_id] = tour
            if min_price == 0 or min_price > tour['price']:
                min_price = tour['price']
            if min_nights == 0 or min_nights > tour['nights']:
                min_nights = tour['nights']
            if max_price < tour['price']:
                max_price = tour['price']
            if max_nights < tour['nights']:
                max_nights = tour['nights']
    # make the first letter of departure lowercase
    dep = data.departures[departure]
    dep = dep.replace(dep[0], dep[0].lower(), 1)

    return render(request, "tours/departure.html", {
        'tours': tours,
        'departure': dep,
        'n_tours': n_tours,
        'min_price': min_price,
        'max_price': max_price,
        'min_nights': min_nights,
        'max_nights': max_nights,
    })


# View for tours
def tour_view(request, id):
    if id not in data.tours:
        raise Http404

    tour = data.tours.get(id)
    # make the first letter of departure lowercase
    dep = data.departures.get(tour['departure'])
    dep = dep.replace(dep[0], dep[0].lower(), 1)

    return render(request, "tours/tour.html", {
        'tour': tour,
        'stars': range(int(tour['stars'])),
        'departure': dep,
    })


def custom_handler404(request, exception):
    logging.warning(f'Non-existent tour was requested {exception}')
    return HttpResponseNotFound('Кажется такая страница не существует :(')


def custom_handler500(request):
    return HttpResponse('Что-то не так. \nКоманда обученных обезьян была отправлена, чтобы разобраться.', status=500)
