from googlemaps import client
from dotenv import load_dotenv
from os import getenv


def configure():
    load_dotenv()


def get_routes_client():
    return client.Client(key=getenv("routes_key"))


def get_dir_client():
    return client.Client(key=getenv("directions_key"))


def get_dist_matrix_client():
    return client.Client(key=getenv("distance_matrix_key"))


def get_geocoding_client():
    return client.Client(key=getenv("geocoding_key"))


def get_unrestricted_client():
    return client.Client(key=getenv("unrestricted_key"))
