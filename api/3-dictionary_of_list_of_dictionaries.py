#!/usr/bin/python3
"""
Creates a dict of lists of dicts
"""
import json
from requests import get


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = get("{}users".format(url)).json()

    all_employed = {}
    for user in users:
        id_user = user.get('id')
        username = user.get('username')
        tasks = get('{}todos?userId={}'.format(url, id_user)).json()
        dict_task = [{"username": username,
                      "task": task['title'],
                      "completed": task['completed']} for task in tasks]
        all_employed[id_user] = dict_task
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(all_employed, file)
