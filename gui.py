from tkinter import Tk, ttk, StringVar

LIST = []

# TODO - Rewrite this function, currently allows the use of the enter key to add items to list
def func(event):
    add_task(task_text_box.getvar('default_var'))


def add_task(text) -> None:
    LIST.append(text)

    task_text_box.setvar('default_var', '' )
    update_tree_box()


def update_tree_box() -> None:

    x = tree_box.get_children()
    for item in x:
        tree_box.delete(item)

    for entry in range(len(LIST)):
        tree_box.insert('', 'end', values=(entry+1, LIST[entry]))


root = Tk()
root.title('TO-DO LIST')
# root.geometry('800x500')

# Frames
list_frame = ttk.Frame(root, padding=2)
list_frame.grid(row=0, column=0, sticky='NSEW')
button_frame = ttk.Frame(root, padding=2)
button_frame.grid(row=1, column=0, sticky='NSEW')

tree_box = ttk.Treeview(list_frame, columns=('1', '2'), show='headings', selectmode='browse')
scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=tree_box.yview)
tree_box.configure(yscrollcommand=scrollbar.set)

tree_box.grid(row=0, column=0, sticky='NSEW')
scrollbar.grid(row=0, column=1, sticky='NSE')

tree_box.heading('1', text='Index')
tree_box.heading('2', text='Task')
# tree_box.heading('1', 'Index')

# Adding a task to the list
default_text = StringVar(None, '', 'default_var')

task_text_box = ttk.Entry(button_frame, textvariable = default_text)
task_text_box.grid(row=0, column=0, sticky='NSEW')

add_button = ttk.Button(button_frame, text='Add', command=lambda :add_task(task_text_box.getvar('default_var')))
add_button.grid(row=0, column=1, sticky='NSEW')


# Enables the ability to add items with the enter key
root.bind('<Return>', func)

# edit_button = ttk.Button(button_frame, text='Edit')
# edit_button.grid(row=0, column=1, sticky='NSEW')

# delete_button = ttk.Button(button_frame, text='Delete')
# delete_button.grid(row=0, column=2, sticky='NSEW')

# completed_button = ttk.Button(button_frame, text='Completed')
# completed_button.grid(row=0, column=3, sticky='NSEW')

# Resize code
root.grid_columnconfigure(0, weight=1)
list_frame.grid_columnconfigure(0, weight=1000)
list_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(0, weight=10)
button_frame.grid_columnconfigure(1, weight=1)

root.grid_rowconfigure(0, weight=8)
root.grid_rowconfigure(0, weight=1)

# Main run
root.mainloop()