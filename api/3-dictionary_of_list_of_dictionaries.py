#!/usr/bin/python3
"""Export all employees' TODO tasks to a JSON file."""

import json
import urllib.request


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    with urllib.request.urlopen(users_url) as response:
        users = json.loads(response.read().decode())

    with urllib.request.urlopen(todos_url) as response:
        tasks = json.loads(response.read().decode())

    all_employees = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        employee_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in tasks
            if task.get("userId") == user.get("id")
        ]

        all_employees[user_id] = employee_tasks

    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(all_employees, json_file)
