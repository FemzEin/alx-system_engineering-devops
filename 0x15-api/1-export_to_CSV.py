#!/usr/bin/python3
"""
Script to retrieve an employee and his/her todo list progress
"""
if __name__ == "__main__":
    import sys
    import requests
    import csv

    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user_url = base_url + "users/{}".format(user_id)
    todos_url = base_url + "todos?userId={}".format(user_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")

    filename = "{}.csv".format(user_id)
    with open(filename, 'w') as f:
        for todo in todos:
            csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            user_id_str = str(user_id)
            completed_str = str(todo.get("completed"))
            task_title = todo.get("title")
            csv_writer.writerow([user_id_str,
                                 username,
                                 completed_str,
                                 task_title])
