import csv

STATUSES_FILE = './data/statuses.csv'
BOARDS_FILE = './data/boards.csv'
CARDS_FILE = './data/cards.csv'
DATA_HEADER = ["id","board_id","title","status_id","order"]
DATA_HEADER2=["id","title"]
_cache = {}  # We store cached data in this dict to avoid multiple file readings


def _read_csv(file_name):
    """
    Reads content of a .csv file
    :param file_name: relative path to data file
    :return: OrderedDict
    """
    with open(file_name) as boards:
        rows = csv.DictReader(boards, delimiter=',', quotechar='"')
        formatted_data = []
        for row in rows:
            formatted_data.append(dict(row))
        return formatted_data


def _get_data(data_type, file, force):
    """
    Reads defined type of data from file or cache
    :param data_type: key where the data is stored in cache
    :param file: relative path to data file
    :param force: if set to True, cache will be ignored
    :return: OrderedDict
    """
    if force or data_type not in _cache:
        _cache[data_type] = _read_csv(file)
    return _cache[data_type]


def clear_cache():
    for k in list(_cache.keys()):
        _cache.pop(k)


def get_statuses(force=False):
    return _get_data('statuses', STATUSES_FILE, force)


def get_boards(force=False):
    return _get_data('boards', BOARDS_FILE, force)


def get_cards(force=False):
    return _get_data('cards', CARDS_FILE, force)


def write_to_file(datafile):
        with open(CARDS_FILE, "w") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=DATA_HEADER)
            writer.writeheader()
            writer.writerows(datafile)


def write_to_boards(datafile):
        with open(BOARDS_FILE, "w") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=DATA_HEADER2)
            writer.writeheader()
            writer.writerows(datafile)


def show_cards():
    with open(CARDS_FILE) as csvfile:
        result = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            new = dict(row)
            result.append(new)
        return result


def show_boards():
    with open(BOARDS_FILE) as csvfile:
        result = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            new = dict(row)
            result.append(new)
        return result