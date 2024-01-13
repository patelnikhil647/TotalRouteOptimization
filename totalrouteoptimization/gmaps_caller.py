from googlemaps import distance_matrix as dm, geocoding as gc
from datetime import datetime
from totalrouteoptimization import config, json_handler


def create_dist_mat(first, second):
    json_file = json_handler.create_filename(first, second)
    now = datetime.now()
    result = dm.distance_matrix(config.get_dist_matrix_client(), first, second, units="imperial", departure_time=now)
    json_handler.echo_to_json(result, json_file)


def create_geocode(location):
    json_file = json_handler.create_filename(location)
    result = gc.geocode(config.get_unrestricted_client(), location)
    json_handler.echo_to_json(result, json_file)
