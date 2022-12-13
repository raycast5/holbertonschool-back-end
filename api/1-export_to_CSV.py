#!/usr/bin/python3
"""
Exports to CSV
"""
import csv
from requests import get
from sys import argv

#  print('HTTP header: ', response.headers)
#  print('URL: ', response.url)
#  print('Status code: ', response.status_code)

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    id_user = argv[1]
    users = get('{}users/{}'.format(url, id_user)).json()
    username = users.get('username')
    tasks = get('{}todos?userId={}'.format(url, id_user)).json()
    with open('{}.csv'.format(id_user), 'wt') as file:
        write_file = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            write_file.writerow([int(id_user), username,
                                task.get('completed'), task.get('title')])
