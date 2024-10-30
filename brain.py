DB_FILE = './todo_list.txt'

def read_db() -> list:
    with open(DB_FILE, 'r') as file:
        lines = file.readlines()
    return lines


def write_db(lines: list) -> None:
    with open(DB_FILE, 'w') as file:
        file.writelines(lines)


def append_db(text: str) ->None:
    with open('./todo_list.txt', 'a') as td_list:
        td_list.write(text + '\n')