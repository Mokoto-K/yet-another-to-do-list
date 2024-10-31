from tkinter import Tk, ttk, StringVar, NO
import brain as brain


# TODO - Rewrite this function, currently allows the use of the enter key to add items to list
def func(event):
    add_task(task_text_box.getvar('default_var'))


def add_task(text: str) -> None:
    # Add the text in the text box to the database
    brain.append_db(text)

    # Reset the txt box to empty for the next input
    task_text_box.setvar('default_var', '' )

    update_tree_box()


def delete_task() -> None:
    # Get a hold of the index of the users selected item to delete
    get_selected_item = tree_box.selection()
    index_of_selected = tree_box.index(get_selected_item[0])

    # Read in all the items in the to do list database
    lines = brain.read_db()
    # Delete the line that matches the index obtained above
    lines.pop(index_of_selected)
    # Rewrite the list to the database without the deleted item
    brain.write_db(lines)

    update_tree_box()


def update_tree_box() -> None:

    # Get all the items displayed in the tree box into a list
    box_items = tree_box.get_children()
    # Iterate through each item in the list and delete them from tree box view
    for item in box_items:
        tree_box.delete(item)

    # Get all the lines written in the database
    lines = brain.read_db()
    # Iterate through each line and add it to the tree box view
    for entry in range(len(lines)):
        tree_box.insert('', 'end', values=(entry+1, lines[entry]))


root = Tk()
root.title('TO-DO LIST')
# root.geometry('800x500')

# Frames
list_frame = ttk.Frame(root, padding=5)
list_frame.grid(row=0, column=0, sticky='NSEW')
button_frame = ttk.Frame(root, padding=5)
button_frame.grid(row=1, column=0, sticky='NSEW')

# Creates the list area to hold the list of to dos and adds a scrollbar
tree_box = ttk.Treeview(list_frame, columns=('1', '2'), show='headings', selectmode='browse', height=10)
scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=tree_box.yview)
tree_box.configure(yscrollcommand=scrollbar.set)

tree_box.grid(row=0, column=0, sticky='NSEW')
scrollbar.grid(row=0, column=1, sticky='NSE')

# Controls the heading names for the columns as well as all variables concerning the columns
tree_box.heading('1', text='#')
tree_box.column('1', minwidth=0, width=20, stretch=NO)
tree_box.heading('2', text='Task')
tree_box.column('2', minwidth=0, width=550, stretch=NO)

# Adding a task to the list
default_text = StringVar(None, '', 'default_var')

# Where you type in  new to do
task_text_box = ttk.Entry(button_frame, textvariable = default_text)
task_text_box.grid(row=0, column=0, sticky='NSEW')
task_text_box.focus_set()

add_button = ttk.Button(button_frame, text='Add', command=lambda :add_task(task_text_box.getvar('default_var')))
add_button.grid(row=0, column=1, sticky='NSEW')

delete_button = ttk.Button(button_frame, text='Delete', command=delete_task)
delete_button.grid(row=0, column=2, sticky='NSEW')

# Enables the ability to add items with the enter key
root.bind('<Return>', func)

# edit_button = ttk.Button(button_frame, text='Edit')
# edit_button.grid(row=0, column=1, sticky='NSEW')

# completed_button = ttk.Button(button_frame, text='Completed')
# completed_button.grid(row=0, column=3, sticky='NSEW')

# Resize code
root.grid_columnconfigure(0, weight=1)
list_frame.grid_columnconfigure(0, weight=1000)
list_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(0, weight=10)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)

root.grid_rowconfigure(0, weight=10)
root.grid_rowconfigure(1, weight=1)

# Main run
update_tree_box()
root.mainloop()