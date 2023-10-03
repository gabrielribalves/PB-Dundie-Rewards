from dundie.utils.log import getLogger

log = getLogger()

def load(filepath):
    """Loads data from filepath to the database.
    >>> len(load('assets/people.csv'))
    2
    """
    try:
        with open(filepath) as file_:
            return [line.strip() for line in file_.readlines()]
    except FileNotFoundError as e:
        log.error(str(e))
        raise e
