#!/usr/bin/python3
"""Export an employee's TODO tasks to a CSV file."""

import csv
import json
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    )

    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode())

    with urllib.request.urlopen(todos_url) as response:
        tasks = json.loads(response.read().decode())

    filename = "{}.csv".format(employee_id)

    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([
                employee_id,
                user.get("username"),
                task.get("completed"),
                task.get("title")
            ])
