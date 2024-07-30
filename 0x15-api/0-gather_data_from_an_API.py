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
    todos_response = requests.get(api_url +
                                  "todos?userId={}".format(employee_id))
    todos_data = todos_response.json()
    completed = []
    for todo in todos_data:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user_data.get("name"), len(completed), len(todos_data)))
    for task in completed:
        print("\t {}".format(task))
