#!/usr/bin/python3
""" Export to JSON"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    req = requests.get(url_user)

    USERNAME = req.json().get('username')

    url_task = url_user + '/todos'
    req = requests.get(url_task)
    tsks = req.json()

    dict_data = {USER_ID: []}
    for tsk in tsks:
        TASK_COMPLETED_STATUS = tsk.get('completed')
        TASK_TITLE = tsk.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    """print(dict_data)"""
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)
