from totalrouteoptimization import gmaps_caller, json_handler


def extreme_pnt_sol(origin, dests, end=None):
    """This solution finds the routes starting from the most cardinally extreme points (i.e. North-most,
    Southeast-most, etc.) and then returns the fastest one. If, there are destinations on the way to an extreme
    point from the origin, then this solution will also consider visiting those first.

    :param origin: The starting location of the route
    :type origin: str

    :param dests: The list of all locations that need to be visited
    :type dests: list

    :param end: If non-null value, will end the route with this location
    :type end: str

    :return: The order in which to visit each location
    :rtype: list
    """
    pass
