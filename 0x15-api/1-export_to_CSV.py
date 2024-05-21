#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    request = requests.get(url_user)
    user_name = request.json().get('username')
    tsk = url_user + '/todos'
    request = requests.get(tsk)
    tsks = request.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for tsk in tsks:
            completed = tsk.get('completed')
            """Complete"""
            title_tsk = tsk.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_tsk))
