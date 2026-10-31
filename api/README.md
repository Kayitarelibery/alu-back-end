# Web Infrastructure – REST API

## About the Project

This project is about learning how to work with APIs using Python. I used the JSONPlaceholder REST API to retrieve information about employees and their tasks.

The main goal was to understand how applications communicate with external services, how to collect information from an API, and how to organize and export that information into CSV and JSON files.

Through this project, I practiced using Python to make API requests, process data, and create files in different formats.

## What I Worked On

The project contains four Python scripts:

### 0. Gather Data from an API
**File:** `0-gather_data_from_an_API.py`

This script takes an employee ID as an argument and retrieves the employee's name and tasks. It then displays the number of completed tasks and lists their titles.

Example:

```bash
./0-gather_data_from_an_API.py 2
```

### 1. Export Data to CSV
**File:** `1-export_to_CSV.py`

This script retrieves all tasks belonging to a specific employee and saves them in a CSV file. The file includes the employee ID, username, task completion status, and task title.

Example:

```bash
./1-export_to_CSV.py 2
```

This creates a file named `2.csv`.

### 2. Export Data to JSON
**File:** `2-export_to_JSON.py`

This script collects all tasks belonging to one employee and saves the information in JSON format.

Example:

```bash
./2-export_to_JSON.py 2
```

This creates a file named `2.json`.

### 3. Export All Employees' Data
**File:** `3-dictionary_of_list_of_dictionaries.py`

This script retrieves information about all employees and their tasks. It organizes the information into a dictionary, with each employee's ID as a key, and saves everything in one JSON file.

Example:

```bash
./3-dictionary_of_list_of_dictionaries.py
```

This creates `todo_all_employees.json`.

## Technologies Used

- Python 3
- REST API
- JSONPlaceholder API
- CSV
- JSON
- Ubuntu Linux

## What I Learned

Working on this project helped me understand how APIs make it possible for different applications to communicate and exchange information.

I also gained practical experience with Python's `urllib`, `json`, and `csv` modules. Most importantly, I learned how to retrieve data, process it, and export it in formats that can be used by other applications.

## Author

**Kayitare Libery**
