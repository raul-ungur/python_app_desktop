import json
import os

def save_task(input_var, input_date_get):
    tasks_json = "tasks.json"
    
    if (os.path.exists(tasks_json)):
        with open(tasks_json, "r") as file:
            try:
                dati = json.load(file)
            except json.JSONDecodeError:
                dati = {}
    else:
        dati = {}


    if input_date_get not in dati:
        dati[input_date_get] = []

    dati[input_date_get].append({
        "input": input_var
    })

    with open(tasks_json, "w") as file:
        json.dump(dati, file, indent=4)

    print("Task salvata")