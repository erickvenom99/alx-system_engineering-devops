#!/usr/bin/env python3
import requests
import json
import sys

if __name__ == "__main__":
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    api_url = 'https://jsonplaceholder.typicode.com/'
    ids = set()
    user_data = res.json()

    export = {}

    for user in user_data:
        ids.add(user.get('userId'))

    for user in ids:
        req = requests.get(api_url + 'users/{}'.format(user))
        username = req.json().get('username')

        res = requests.get(api_url + 'todos?userId={}'.format(user))
        todos_data = res.json()

        tasks = []
        for task in todos_data:
            tasks.append({'task': task.get('title'), 'completed':
                         task.get('completed'), 'username': username})
        export[str(user)] = tasks

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump({int(v): export[v] for v in export.keys()}, outfile,
                  sort_keys=True, indent=4)
