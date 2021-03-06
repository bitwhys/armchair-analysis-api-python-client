from armchair_analysis_api_python_client import datatypes
from armchair_analysis_api_python_client.endpoints import request


# TODO: for all functions with pagination below, if no pagination is supplied, get all data

def get_generic(url, class_type, params=None):
    items = []

    r = request.get(url, params=params)

    if 'data' in r.json():
        for item in r.json()['data']:
            items.append(class_type(item))

    return items


def get_parameters(count=None, start=None):
    params = {}

    if count is not None:
        params["count"] = count

    if start is not None:
        params["start"] = start

    return params


def get_active_players(count=None, start=None):
    params = get_parameters(count, start)
    params["status"] = "active"
    url = "http://armchairanalysis.com/api/1.0/players"

    return get_generic(url, datatypes.Player, params=params)


def get_all_players(count=None, start=None):
    params = get_parameters(count, start)
    url = "http://armchairanalysis.com/api/1.0/players"

    return get_generic(url, datatypes.Player, params=params)
