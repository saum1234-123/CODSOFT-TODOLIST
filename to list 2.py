import tkinter as tk

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append([task, False])     # [task_text, done_status]
        entry.delete(0, tk.END)
        show_tasks()

def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index][1] = True
        show_tasks()
    except:
        pass

def show_tasks():
    listbox.delete(0, tk.END)
    for text, done in tasks:
        mark = "✔" if done else "✗"
        listbox.insert(tk.END, f"[{mark}] {text}")

root = tk.Tk()
root.title("Easy To-Do List")

entry = tk.Entry(root, width=35)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Mark Done", command=mark_done).pack()

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

root.mainloop()
