import gmaps_caller
import json_handler


def backtracking_sol(origin, dests, end):
    """More efficient solution to Total Route Problem. Starting from the end of the route, backtrack by finding the
    most efficient route from all destinations to the end. Once found, treat that destination as the "current end" and
    find the most efficient route from all remaining destinations to the current end. Repeat until there are no
    remaining destinations.
    As of current, will not always return a correct result. Additionally, this solution requires an end variable
    whereas my original plan for the solution is that the end parameter is defaulted and not necessary.
    Time Complexity: O(n^2)

    :param origin: The starting location of the route
    :type origin: str

    :param dests: The list of all locations that need to be visited
    :type dests: list

    :param end: End the route with this location
    :type end: str

    :return: the order in which to visit each location
    :rtype: list
    """
    ret_route = [end]  # initialize the return list with the final destination
    uninserted_dests = dests  # destinations that have not yet been inserted into the return list

    while len(uninserted_dests) > 0:
        curr_end = ret_route[0]
        lowest = -1
        next_end = uninserted_dests[0]  # redundant variable assignment but necessary so warning doesn't show
        for loc in uninserted_dests:  # for each uninserted destination, find most time efficient to curr_end
            file = json_handler.create_filename(loc, curr_end)
            if not json_handler.does_file_exist(file):  # creates dist_mat if not created before
                gmaps_caller.create_dist_mat(loc, curr_end)
            dur_val = json_handler.read_duration_value(file)  # read the duration value from dist_mat file
            if dur_val["value"] < lowest or lowest < 0:  # if duration is less than lowest or if this is first loop iter
                lowest = dur_val["value"]  # set lowest to the current duration
                next_end = loc  # next_end will be curr_end in next iteration
        ret_route.insert(0, next_end)
        uninserted_dests.remove(next_end)

    ret_route.insert(0, origin)
    return ret_route
