from itertools import permutations
from totalrouteoptimization import gmaps_caller, json_handler


def naive_sol(origin, dests, end=None):
    """Naive solution to Total Route Problem. Finds the total duration of each permutation of routes and returns the
    smallest one.
    Time Complexity: O(n!)

    :param origin: The starting location of the route
    :type origin: str

    :param dests: The list of all locations that need to be visited
    :type dests: list

    :param end: If non-null value, will end the route with this location
    :type end: str

    :return: The order in which to visit each location
    :rtype: list
    """
    curr = 0
    lowest = -1
    ret_route = []
    perm_dests = permutations(dests)  # iterator of permutations of the dests list

    for perm in perm_dests:
        perm = list(perm)  # converting each permutation from tuple to list is easier to work with
        perm.insert(0, origin)  # insert origin to beginning of list
        if end is not None:
            perm.append(end)  # insert end to end of list if it exists

        for i in range(len(perm) - 1):  # for each location in this permutation
            file = json_handler.create_filename(perm[i], perm[i + 1])
            if not json_handler.does_file_exist(file):  # creates dist_mat if not created before
                gmaps_caller.create_dist_mat(perm[i], perm[i + 1])
            dur_val = json_handler.read_duration_value(file)  # reads duration value given in seconds
            curr += dur_val["value"]  # add duration value to current total

        if curr < lowest or lowest < 0:  # if current total is less than lowest or if this is first iteration of loop
            lowest = curr
            ret_route = perm  # set route to return to this permutation
        curr = 0  # reset current duration value total

    return ret_route
