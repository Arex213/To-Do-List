import tkinter as tk
import tkinter.messagebox as messagebox

# Set up the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("800x600")

# Title label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 32))
title_label.pack(pady=20)

# Create entry field
entry = tk.Entry(root, font=("Arial", 24))
entry.pack(pady=20)

# Initialize color index and colors
color_index = 0
colors = ["black","red", "green", "blue"]


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                parts = line.strip().split("||")
                if len(parts) == 2:
                    task, color = parts
                    listbox.insert(tk.END, task)
                    listbox.itemconfig(tk.END, fg=color)
                else:
                    task = parts[0]
                    listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass  

def save_tasks():
    with open("tasks.txt", "w") as file:
        for i in range(listbox.size()):
            task = listbox.get(i)
            color = listbox.itemcget(i, "fg")
            file.write(f"{task}||{color}\n")

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        listbox.itemconfig(tk.END, fg=colors[color_index])
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_indices = listbox.curselection()
    if selected_task_indices:
        for i in reversed(selected_task_indices):
            listbox.delete(i)
        save_tasks()

def save_and_quit():
    save_tasks()
    root.quit()

def change_color():
    global color_index
    color_index = (color_index + 1) % len(colors)
    entry.configure(fg=colors[color_index])

# Create buttons
add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 18))
add_button.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=("Arial", 18))
remove_button.pack(pady=10)

color_button = tk.Button(root, text="Change Color", command=change_color, font=("Arial", 18))
color_button.pack(pady=10)

save_buttton = tk.Button(root, text="Save Tasks and Quit", command=save_and_quit, font=("Arial", 18))
save_buttton.pack(pady=10)

# Create listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 24))
listbox.pack(pady=20)

load_tasks()

root.protocol("WM_DELETE_WINDOW", lambda: on_close())

def on_close():
    if messagebox.askokcancel("Quit", "Do you want to save your tasks?"):
        save_tasks()
    root.quit()

root.mainloop()
