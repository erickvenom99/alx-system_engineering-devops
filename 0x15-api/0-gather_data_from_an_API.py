#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
"""
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the command line arguments
    employee_id = sys.argv[1]

    # Set the URL for the JSONPlaceholder API
    api_url = "https://jsonplaceholder.typicode.com/"

    # Get the employee's information
    req = requests.get(api_url + "users/{}".format(employee_id))
    user_data = req.json()

    # Get the employee's to-do list
    todos_response = requests.get(api_url +
                                  'todos?userId={}'.format(employee_id))
    todos_data = todos_response.json()

    # Find completed tasks
    completed = []
    for todo in todos_data:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    # Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks ({}/{}):"
          .format(user_data.get("name"), len(completed), len(todos_data)))

    # Print each completed task
    for task in completed:
        print("\t{}".format(task))
