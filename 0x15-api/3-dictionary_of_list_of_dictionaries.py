#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""
import json
import requests
import sys

if __name__ == "__main__":
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    api_url = 'https://jsonplaceholder.typicode.com/'
    unique_ids = set()
    user_data = res.json()
    for user in user_data:
        unique_ids.add(user.get('userId'))     
    export = {}
    for user in unique_ids:
        req = requests.get(api_url + 'users/{}'.format(user))
        username = req.json().get('username')

        res = requests.get(api_url + 'todos?userId={}'.format(user))
        todos_data = res.json()

        export['{}'.format(user)] = []
        for task in todos_data:
            export['{}'.format(user)].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
                })

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump({int(v): export[v] for v in export.keys()}, outfile,
                  sort_keys=True, indent=4)
