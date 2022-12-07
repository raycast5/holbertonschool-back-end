#!/usr/bin/python3
"""Script uses employee ID, returns information about todo list progress."""

from sys import argv
import json
import requests


if __name__ == "__main__":
    """This function retrives to do lists by employee"""
    name_source = requests.get(f"https://jsonplaceholder.typicode.com/users" +
                               f"/{argv[1]}")
    employees = name_source.json()
    task_source = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = task_source.json()

    total_tasks = 0
    tasks_comp = 0
    user_id = int(argv[1])
    user_name = employees.get('name')
    task_list = []

    for tasks in todos:
        if tasks.get('userId') == user_id:
            total_tasks += 1
            if tasks.get("completed") is True:
                tasks_comp += 1
                task_list.append(tasks.get("title"))

    print(f"Employee {user_name} is done with tasks " +
          f"({tasks_comp}/{total_tasks}):")
    for task in task_list:
        print(f"\t {task}")
