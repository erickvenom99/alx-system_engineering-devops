#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
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

    with open("{}.csv".format(user_id), 'w', newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow([user_id, username, task.get("completed"),
                            task.get("title")])
