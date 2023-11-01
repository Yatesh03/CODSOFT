import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and place the widgets
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
clear_button.pack()

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

# Start the GUI event loop
root.mainloop()
