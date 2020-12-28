import logging
import random

from django.http import HttpResponse
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render

import tours.data as data

NUMBER_OF_TOURS_ON_MAIN = 6  #


# View for main page
def main_view(request):
    # create dict of random tours for main page
    random_keys = random.sample(data.tours.keys(), k=NUMBER_OF_TOURS_ON_MAIN)
    random_list = {tour_id: tour for tour_id, tour in data.tours.items() if tour_id in random_keys}

    return render(request, "index.html", {
        'subtitle': data.subtitle,
        'description': data.description,
        'random_list': random_list,
    })


# View for page by departure
def departure_view(request, departure):
    min_price, max_price, min_nights, max_nights = (0, 0, 0, 0)
    tours = {}
    for tour_id, tour in data.tours.items():
        if tour['departure'] == departure:
            tours[tour_id] = tour
            if min_price == 0:
                min_price = tour['price']
            else:
                min_price = min(min_price, tour['price'])
            if min_nights == 0:
                min_nights = tour['nights']
            else:
                min_nights = min(min_nights, tour['nights'])
            max_price = max(max_price, tour['price'])
            max_nights = max(max_nights, tour['nights'])

    if not any(tours):
        raise Http404

    # make the first letter lowercase
    dep = data.departures[departure]
    dep = dep.replace(dep[0], dep[0].lower(), 1)

    return render(request, "tours/departure.html", {
        'tours': tours,
        'departure': dep,
        'n_tours': len(tours),
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
    # make the first letter lowercase
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
