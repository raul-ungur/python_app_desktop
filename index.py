import tkinter as tk

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x300")


#input = StringVar()

input_var = tk.StringVar()
task_entry = tk.Entry(root,textvariable = input_var, font=('calibre',10,'normal'))
task_entry.grid(row=0, column=0, padx=10, pady=10)
def show_input():
    input_get = input_var.get()
    input_view = tk.Label(root, text= input_get, font=('calibre',10,'normal'))
    input_view.grid(row=1, column=0, padx=10, pady=10) 
    def remove_task():
        input_view.config(text="")
        button_remove.destroy()  
    button_remove = tk.Button(root, text= "remove task", command= remove_task )
    button_remove.grid(row=1, column=1, padx=10, pady=10)

button = tk.Button(root, text= "add task", command= show_input )
button.grid(row=0, column=1, padx=10, pady=10)
root.mainloop()