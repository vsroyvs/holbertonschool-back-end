#!/usr/bin/python3
"""Script to export data in a CSV format"""
import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(f'{url}/users/{user_id}').json()
    to_do = requests.get(f'{url}/todos?userId={user_id}').json()

    filename = f'{user_id}.csv'

    with open(filename, mode='w', newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in to_do:
            writer.writerow([user['id'], user['username'],
                            str(todo['completed']), todo['title']])
