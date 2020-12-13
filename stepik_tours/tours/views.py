from django.shortcuts import render


# View for main page
def main_view(request):
    return render(request, "index.html")


# View for page by departure
def departure_view(request, departure):
    return render(request, "tours/departure.html")


# View for tours
def tour_view(request, id):
    return render(request, "tours/tour.html")
