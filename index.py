import tkinter as tk

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x300")

input_var = tk.StringVar()
task_entry = tk.Entry(root,textvariable = input_var, font=('calibre',10,'normal'))
task_entry.pack()
button = tk.Button(root, text= "add task", command= lambda: show_input())
button.pack()


def show_input():
    frame = tk.Frame(root, bg="blue")
    frame.pack(fill=tk.X, padx=5, pady=5)
    input_get = input_var.get()
    input_view = tk.Label(frame, text= input_get, font=('calibre',10,'normal'))
    input_view.pack(side=tk.LEFT, padx=5, pady=5) 
    def remove_task():
        frame.destroy()  
    
    button_remove = tk.Button(frame, text= "remove task", command= remove_task )
    button_remove.pack(side=tk.RIGHT, padx=5, pady=5)



root.mainloop()