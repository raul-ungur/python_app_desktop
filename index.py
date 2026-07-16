import tkinter as tk
import database 
import ui

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
###


def def_but_add_task():
    input_date_get = input_date.get()
    show_input()
    database.save_task(input_get, input_date_get)





def show_input():
    global input_get
    input_get = input_var.get()
    frame = tk.Frame(pag2, bg="blue")
    frame.pack(fill=tk.X, padx=5, pady=5)
    input_view = tk.Label(frame, text= input_get, font=('calibre',10,'normal'))
    input_view.pack(side=tk.LEFT, padx=5, pady=5) 
    def remove_task():
        frame.destroy()  
    
    button_remove = tk.Button(frame, text= "remove task", command= remove_task )
    button_remove.pack(side=tk.RIGHT, padx=5, pady=5)

root.mainloop()
