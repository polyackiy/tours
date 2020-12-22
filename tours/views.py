from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.http import HttpResponse

import tours.data as data


# View for main page Потом надо удалиь лишние
def main_view(request):
    return render(request, "index.html", {
        'title': data.title,
        'subtitle': data.subtitle,
        'description': data.description,
        'departures': data.departures,
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
    return render(request, "tours/tour.html", {
        'title': data.title,
        'subtitle': data.subtitle,
        'description': data.description,
        'departures': data.departures,
        'tours': data.tours,
    })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Кажется такая страница не существует :(')


def custom_handler500(request):
    return HttpResponse('Что-то не так. \nКоманда обученных обезьян была отправлена, чтобы разобраться.', status=500)
