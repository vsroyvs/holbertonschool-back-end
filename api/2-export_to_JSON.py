#!/usr/bin/python3
"""returning info from Rest Api"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(f'{url}/users/{user_id}').json()
    to_do = requests.get(f'{url}/todos?userId={user_id}').json()

    todos_user = [{
        "task": todo["title"],
        "completed": todo["completed"],
        "username":user["username"]} for todo in to_do]
    display_todo = {user_id: todos_user}
    filename = f'{user_id}.json'

    with open(filename, mode='w', newline="") as json_file:
        json.dump(display_todo, json_file)
