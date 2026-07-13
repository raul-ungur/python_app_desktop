import tkinter as tk

from flask import json

import os

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x300")

pag1 = tk.Frame(root,bg="red")
pag1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10, )

pag2 = tk.Frame(root,bg="green")

### pagina 1
go_pag2 = tk.Button(pag1, text= "add task", command= lambda: def_go_pag2())
go_pag2.pack()
def def_go_pag2():
  pag1.pack_forget()
  pag2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
###


### pagina 2
input_var = tk.StringVar()
task_entry = tk.Entry(pag2,textvariable = input_var, font=('calibre',10,'normal'))
task_entry.pack()
button = tk.Button(pag2, text= "add task", command= lambda: show_input())
button.pack()
go_pag1 = tk.Button(pag2, text= "view tasks", command= lambda: def_go_pag1())
go_pag1.pack()
def def_go_pag1():
  pag2.pack_forget()
  pag1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
###






def show_input():
    input_get = input_var.get()
    task_json = "task.json"
    frame = tk.Frame(pag2, bg="blue")
    frame.pack(fill=tk.X, padx=5, pady=5)

    input_view = tk.Label(frame, text= input_get, font=('calibre',10,'normal'))
    input_view.pack(side=tk.LEFT, padx=5, pady=5) 
    def remove_task():
        frame.destroy()  
    
    button_remove = tk.Button(frame, text= "remove task", command= remove_task )
    button_remove.pack(side=tk.RIGHT, padx=5, pady=5)

    if (os.path.exists(task_json)):
        with open(task_json, "r") as file:
            try:
                dati = json.load(file)
            except json.JSONDecodeError:
                dati = []
    else:
        dati = []

    dati.append(input_get)
    with open(task_json, "w") as file:
        json.dump(dati, file)
    print("Task saved to task.json")




root.mainloop()