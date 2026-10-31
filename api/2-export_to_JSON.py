#!/usr/bin/python3
"""Export an employee's TODO tasks to a JSON file."""

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

    data = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            }
            for task in tasks
        ]
    }

    filename = "{}.json".format(employee_id)

    with open(filename, mode="w") as json_file:
        json.dump(data, json_file)
