import tours.data as data


def menu_data(request):
    return {
        'title': data.title,
        'departures': data.departures,
    }
