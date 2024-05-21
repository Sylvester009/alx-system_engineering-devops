#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(url)
    Users = res.json()

    users_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        url = url + '/todos/'
        res = requests.get(url)

        tsks = res.json()
        users_dict[USER_ID] = []
        for tsk in tsks:
            TASK_COMPLETED_STATUS = tsk.get('completed')
            TASK_TITLE = tsk.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
