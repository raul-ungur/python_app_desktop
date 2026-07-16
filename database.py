import json
import os


def save_task(input_var, input_date):
    tasks_json = "tasks.json"

    if (os.path.exists(tasks_json)):
        with open(tasks_json, "r") as file:
            try:
                dati = json.load(file)
            except json.JSONDecodeError:
                dati = []
    else:
        dati = []

    dati.append({input_date : {"input": input_var}})
    with open(tasks_json, "w") as file:
        json.dump(dati, file)
    print("Task saved to tasks.json")