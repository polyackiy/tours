from django.shortcuts import render
from django.http import HttpResponseNotFound


# View for main page
def main_view(request):
    return render(request, "index.html")


# View for page by departure
def departure_view(request, departure):
    return render(request, "tours/departure.html")


# View for tours
def tour_view(request, id):
    return render(request, "tours/tour.html")


def custom_handler404(request, exception):
    return HttpResponseNotFound('Кажется такая страница не существует :(')


def custom_handler500(request):
    return HttpResponseNotFound('Что-то не так. \nКоманда обученных обезьян была отправлена, чтобы разобраться.')
