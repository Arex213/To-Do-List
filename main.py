import tkinter as tk
import tkinter.messagebox as messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("800x600")

# Create entry field
entry = tk.Entry(root, font=("Arial", 24))
entry.pack(pady=20)

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass  # It's okay if the file doesn't exist yet

# Function to save tasks to the text file
def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write("-" + task + "\n")

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
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

# Create buttons
add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 18))
add_button.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=("Arial", 18))
remove_button.pack(pady=10)

save_buttton = tk.Button(root, text="Save Tasks", command=save_tasks, font=("Arial", 18))
save_buttton.pack(pady=10)

# Create listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 24))
listbox.pack(pady=20)

load_tasks()

root.protocol("WM_DELETE_WINDOW", lambda: on_close())

def on_close():
    if messagebox.askokcancel("Quit", "Do you want to save your tasks?"):
        save_tasks()
    root.destroy()

root.mainloop()
