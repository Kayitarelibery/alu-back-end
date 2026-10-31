#!/usr/bin/python3

import sys
import urllib.request
import json


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

    employee_name = user.get("name")
    completed_tasks = [task for task in tasks if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(completed_tasks), len(tasks)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
