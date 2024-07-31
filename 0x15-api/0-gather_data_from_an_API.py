#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
"""
import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]

    api_url = "https://jsonplaceholder.typicode.com/"

    req = requests.get(api_url + "users/{}".format(employee_id))
    user_data = req.json()
    employeeName = user_data.get("name")
    todos_response = requests.get(api_url +
                                  "todos?userId={}".format(employee_id))
    todos_data = todos_response.json()
    complete, total = 0
    for task in todos_data:
        total += 1
        if task.get('completed'):
            complete += 1
    print('Employee {} is done with tasks({}/{}):'.format(employeeName,
                                                          complete, total))
    for task in todos_data:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
