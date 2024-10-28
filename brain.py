from tkinter import Tk, ttk


root = Tk()
root.title('TO-DO LIST')
root.geometry('800x500')

# Frames
list_frame = ttk.Frame(root, padding=2)
list_frame.grid(row=0, column=0, sticky='NSEW')
button_frame = ttk.Frame(root, padding=2)
button_frame.grid(row=1, column=0, sticky='NSEW')

treemans = ttk.Treeview(list_frame)

# Buttons
add_button = ttk.Button(button_frame, text='Add')
add_button.grid(row=0, column=0, sticky='NSEW')

edit_button = ttk.Button(button_frame, text='Edit')
edit_button.grid(row=0, column=1, sticky='NSEW')

delete_button = ttk.Button(button_frame, text='Delete')
delete_button.grid(row=0, column=2, sticky='NSEW')

completed_button = ttk.Button(button_frame, text='Completed')
completed_button.grid(row=0, column=3, sticky='NSEW')

# Resize code
root.grid_columnconfigure(0, weight=1)

root.grid_rowconfigure(0, weight=8)
root.grid_rowconfigure(0, weight=1)

# Main run
root.mainloop()