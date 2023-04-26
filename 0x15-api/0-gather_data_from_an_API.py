#!/usr/bin/python3
"""
Python script that Gather data from an API
"""
import requests
import sys


if __name__ == '__main__':

    id_c = sys.argv[1]
    task_title = []
    complete = 0
    total_task = 0
    user_url = "https://jsonplaceholder.typicode.com/users/" + id_c
    res = requests.get(user_url).json()
    name = res.get('name')
    task_url = "https://jsonplaceholder.typicode.com/todos/"
    res = requests.get(task_url).json()
    for i in res:
        if i.get('userId') == int(id_c):
            if i.get('completed') is True:
                task_title.append(i['title'])
                complete += 1
            total_task += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, complete, total_task))
    for x in task_title:
        print("\t {}".format(x))
