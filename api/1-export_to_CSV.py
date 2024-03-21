#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export data in the CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    # Define the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from the API
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user.get("username")

    # Fetch the to-do list items associated
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Use list comprehension to iterate over the to-do list items
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
