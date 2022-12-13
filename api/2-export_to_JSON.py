#!/usr/bin/python3
"""
Exports to json in specific format
"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    id_user = argv[1]
    users = get('{}users/{}'.format(url, id_user)).json()
    username = users.get('username')
    tasks = get('{}todos?userId={}'.format(url, id_user)).json()

    listof_task = []
    for task in tasks:
        dict_task = {"task": task['title'],
                     "completed": task['completed'],
                     "username": username}
        listof_task.append(dict_task)
    datas = {str(id_user): listof_task}
    filename = '{}.json'.format(id_user)
    with open(filename, 'w') as file:
        json.dump(datas, file)
