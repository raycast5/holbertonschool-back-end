#!/usr/bin/python3
"""This module has a script that using a REST API, for a given
    employee ID, returns information about his/her TODO list progress."""
from sys import argv
import json
import requests


if __name__ == "__main__":
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
        if user_id == user.get('id'):
            user_name = user.get('name')

    for tasks in todos:
        if tasks.get('userId') == user_id:
            total_tasks += 1
            if tasks.get("completed") is True:
                tasks_comp += 1
                task_list.append(tasks.get("title"))

    print(f"Employee {user_name} is done with tasks" +
          f"({tasks_comp}/{total_tasks}):")
    for task in task_list:
        print(f"\t {task}")
