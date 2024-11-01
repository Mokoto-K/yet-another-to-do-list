DB_FILE = 'database.txt'

def read_from_db() -> list:
    """Read in all lines from the default database file"""
    with open(DB_FILE, 'r') as file:
        lines = file.readlines()
    return lines


def write_to_db(lines: list) -> None:
    """Write the passed in list to a database file"""
    with open(DB_FILE, 'w') as file:
        file.writelines(lines)


def append_to_db(todo: str) ->None:
    """
    Specifically used for the multi functional purpose of being able to add to the
    existing db file or create a new db file if one does not exist
    """
    with open(DB_FILE, 'a') as td_list:
        td_list.write(todo + '\n')