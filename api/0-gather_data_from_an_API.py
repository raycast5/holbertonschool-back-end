#!/usr/bin/tylepython3
"""This module has a script that using a REST API, for a given
    employee ID, returns information about his/her TODO list progress."""
import json
import requests
from sys import argv


name_source = requests.get(f"https://jsonplaceholder.typicode.com/users")
employees = json.loads(name_source.text)
task_source = requests.get(f"https://jsonplaceholder.typicode.com/todos")
todos = json.loads(task_source.text)

total_tasks = 0
tasks_comp = 0
user_id = int(argv[1])
user_name = ""
task_list = []

for user in employees:
    if user_id == user['id']:
        user_name = user['name']

for tasks in todos:
    if int(tasks['userId']) == user_id:
        total_tasks += 1
        if tasks["completed"] is True:
            tasks_comp += 1
            task_list.append(tasks["title"])

print(f"Employee {user_name} is done with tasks ({tasks_comp}/{total_tasks}):")
for task in task_list:
    print(f"\t {task}")
