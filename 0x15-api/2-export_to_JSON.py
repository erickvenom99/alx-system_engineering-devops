#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    # Get the employee ID from the command line arguments
    user_id = sys.argv[1]

    # Set the URL for the JSONPlaceholder API
    api_url = "https://jsonplaceholder.typicode.com/"

    # Get the employee's information
    req = requests.get(api_url + "users/{}".format(user_id))
    user_data = req.json()

    username = user_data.get("username")

    # Get the employee's to-do list
    todos_response = requests.get(api_url + 'todos?userId={}'.format(user_id))
    todos_data = todos_response.json()

    # Prepare the data for JSON export
    json_data = {}
    json_data["{}".format(user_id)] = []
    for task in todos_data:
        json_data["{}".format(user_id)].append(
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            })

    # Write the JSON data to a file
    with open(f"{user_id}.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)
