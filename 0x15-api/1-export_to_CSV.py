#!/usr/bin/python3
"""
Python script that, using REST API,
export data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    id_c = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + id_c
    res = requests.get(user_url).json()
    username = res.get("username")
    req = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (id_c) + '/todos')
    with open("{}.csv".format(sys.argv[1]), "w") as file_c:
        writer = csv.writer(file_c, quoting=csv.QUOTE_ALL)
        for task in req.json():
            writer.writerow([id_c, username,
                            task.get("completed"), task.get("title")])
