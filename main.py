import readline

# CCurrently in a CLI mock up phase of how I want this to look, will convert this all to gui next
TO_DO_LIST: list = []
COMPLETED_TASKS: list = []


def get_commands() -> None:
    print('add - adds a new task to your to-do list')
    print('delete - deletes a task from your to-do list')
    print('edit - edit the contents of a task')


def add_task() -> None:
    add_question: str = input('Add something to do \n')
    TO_DO_LIST.append(add_question)


def delete_task() -> None:
    deleted_task: bool = False

    # Control input
    while not deleted_task:
        if len(TO_DO_LIST) < 1:
            print('There are no tasks to remove')
            break
        else:
            # to stop the except index error from complaining (poor design on my behalf obs)
            delete_question = 0
            try:
                delete_question: int = int(input('Which to-do number would you like to remove?\n'))

                # Control for lower bounds of list index
                if delete_question < 1:
                    print('Please enter an integer greater than 0')
                else:
                    TO_DO_LIST.pop(int(delete_question) - 1)
                    deleted_task = True

            # Control for strings instead of ints and numbers outside of the list length
            except ValueError:
                print('Please enter the integer index number of a task you wish to delete')
            except IndexError:
                print(f'Task index number: {delete_question} doesnt exist, please enter the index number of a '
                      f'task you wish to delete')


def edit_task() -> None:
    edit_question: int = int(input('Which task number would you like to edit')) - 1

    TO_DO_LIST.pop(edit_question)

    edited_task: str = input('What would you like to edit this to do too?\n')

    TO_DO_LIST.insert(edit_question, edited_task)

def display_to_dos() -> None:
    for num in range(len(TO_DO_LIST)):
        print(f'{num + 1}: {TO_DO_LIST[num]}')


def get_marching_orders() -> str:
    question: str = input('What would you like to do? \n')
    return question


def incorrect_input(question: str) -> None:
    print(f'"{question}" is not a valid command, possible commands are:')
    get_commands()


def main() -> None:

    while True:
        display_to_dos()
        question = get_marching_orders()

        # Lists all commands for the user
        if question == 'cmd':
            get_commands()

        # add a task to do
        elif question == 'add':
            add_task()

        # Delete a task
        elif question == 'delete':
            delete_task()

        elif question == 'edit':
            edit_task()

        else:
            incorrect_input(question)


if __name__ == '__main__':
    main()