from googlemaps import distance_matrix as dm
from datetime import datetime
import config
import json_handler


def create_dist_mat(first, second):
    json_file = json_handler.create_filename(first, second)
    now = datetime.now()
    result = dm.distance_matrix(config.get_dist_matrix_client(), first, second, units="imperial", departure_time=now)
    json_handler.echo_to_json(result, json_file)
