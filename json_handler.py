import json
import os


def echo_to_json(obj, file_to_write):
    """Writes json output to a json file.

    :param obj: Object in json formatting to be inputted into a json file
    :type obj: list

    :param file_to_write: File to write to in "json_files/" folder
    :type file_to_write: str

    :return: None
    """
    json_dir = establish_json_dir()
    json_str = json.dumps(obj, indent=4)

    # create filename to write json string into
    filename = json_dir + file_to_write
    with open(filename, 'w') as f:
        f.write(json_str)


def read_from_dist_mat(json_file):
    """Reads data from a given json file holding distance_matrix data

    :param json_file: The name of the json file
    :type json_file: str

    :return: Dictionary if json data is correct, false otherwise
    :rtype: dict or bool
    """
    json_dir = establish_json_dir()
    filename = json_dir + json_file
    with open(filename, 'r') as f:
        data = json.load(f)

    row_elements = data["rows"][0]["elements"][0]
    if row_elements.get("status") == "OK":
        return row_elements
    return False


def read_duration_value(json_file):
    """Reads the duration_in_traffic attributes from the json file holding distance_matrix data

    :param json_file: The name of the json file
    :type json_file: str

    :return: Dictionary of text and value attributes of duration_in_traffic if status is OK, false otherwise
    :rtype: dict or bool
    """
    data = read_from_dist_mat(json_file)
    if not data:
        return False
    return data["duration_in_traffic"]


def read_distance_value(json_file):
    """Reads the distance attributes from the json file holding distance_matrix data

        :param json_file: The name of the json file
        :type json_file: str

        :return: Dictionary of text and value attributes of distance if status is OK, false otherwise
        :rtype: dict or bool
        """
    data = read_from_dist_mat(json_file)
    if not data:
        return False
    return data["distance"]


def establish_json_dir():
    """Create "json_files/" directory if it doesn't exist

    :return: The path of the directory established
    :rtype: str
    """
    json_dir = "json_files/"
    # check if "json_files/" directory exists and if not, create that directory
    if not os.path.exists(json_dir):
        os.makedirs(json_dir)

    return json_dir


def does_file_exist(json_file):
    """Asserts whether a given json file already exists

    :param json_file: The file to assert existence
    :type json_file: str

    :return: True if the file exists, false if not
    :rtype: bool
    """
    json_dir = establish_json_dir()
    filename = json_dir + json_file
    if os.path.exists(filename):
        return True
    else:
        return False


def create_filename(first, second):
    """Creates the standard names of distance matrix json files

    :param first: The starting location
    :type first: str

    :param second: The second location
    :type second: str

    :return: The standardized filename
    :rtype: str
    """
    return first + "_to_" + second + ".json"
