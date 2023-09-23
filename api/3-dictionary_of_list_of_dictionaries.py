#!/usr/bin/python3
"""returning info from Rest Api
all tasks from all employees"""
import json
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(f'{url}/users').json()
    display_todo_all = {}

    for user in users:
        user_id = user['id']
        to_do = requests.get(f'{url}/todos?userId={user_id}').json()
        todos_user = [{
            "username": user["username"],
            "task": todo["title"],
            "completed": todo["completed"]} for todo in to_do]
        display_todo_all[user_id] = todos_user

    filename = f'todo_all_employees.json'

    with open(filename, mode='w', newline="") as json_file:
        json.dump(display_todo_all, json_file)
