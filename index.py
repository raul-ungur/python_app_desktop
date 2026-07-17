import tkinter as tk
import database 

dati = database.load_tasks()

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x300")

pag1 = tk.Frame(root,bg="red")
pag1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10, )

pag2 = tk.Frame(root,bg="green")

### pagina 1
#label_tasks = tk.Label(pag1, text=database.tasks_list, font=('calibre',10,'normal'))
#label_tasks.pack()
go_pag2 = tk.Button(pag1, text= "add task", command= lambda: def_go_pag2())
go_pag2.pack()
def def_go_pag2():
  pag1.pack_forget()
  pag2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

task_frame = tk.Frame(pag1, bg="lightgray")
task_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

def refresh_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for date, tasks in database.tasks_list.items():
        date_label = tk.Label(task_frame, text=f"Date: {date}", font=('calibre',10,'normal'))
        date_label.pack(anchor='w')

        for task in tasks:
            task_label = tk.Label(task_frame, text=f"- {task['input']}", font=('calibre',10,'normal'))
            task_label.pack(anchor='w')


for data, lista_task in dati.items():
    data_label = tk.Label(task_frame, text=f"Date: {data}", font=('calibre',10,'normal'))
    data_label.pack(anchor='w')

    for task in lista_task:
        task_label = tk.Label(task_frame, text=f"- {task['input']}", font=('calibre',10,'normal'))
        task_label.pack(anchor='w')
###

### pagina 2
input_var = tk.StringVar()
task_entry = tk.Entry(pag2,textvariable = input_var, font=('calibre',10,'normal'))
task_entry.pack()
button = tk.Button(pag2, text= "add task", command= lambda: def_but_add_task())
button.pack()
go_pag1 = tk.Button(pag2, text= "view tasks", command= lambda: def_go_pag1() )
go_pag1.pack()
input_date = tk.StringVar()
date_entry = tk.Entry(pag2,textvariable = input_date, font=('calibre',10,'normal'))
date_entry.pack()
def def_go_pag1():
  pag2.pack_forget()
  pag1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
  label_tasks.config(text=database.tasks_list)
  
  
   
###


def def_but_add_task():
    input_date_get = input_date.get()
    input_get = input_var.get()
    database.save_task(input_get, input_date_get)
    tk.Label(pag2, text="Task salvata", font=('calibre',10,'normal')).pack( padx=10, pady=15)






root.mainloop()
