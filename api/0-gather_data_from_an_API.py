#!/usr/bin/python3
"""returning info from Rest Api"""
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{url}/users/{user_id}'
    to_do_url = f'{url}/todos?userId={user_id}'

    user = requests.get(user_url).json()
    to_do = requests.get(to_do_url).json()

    total_tasks = len(to_do)
    completed_tasks = sum(1 for todo in to_do if todo['completed'])
    employee_name = user.get("name")

    print("Employee {} is done with tasks({}/{}):".format(
          employee_name, completed_tasks, total_tasks))
    [print(f"\t {todo['title']}") for todo in to_do if todo['completed']]
