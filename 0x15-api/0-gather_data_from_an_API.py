#!/usr/bin/python3
"""
Script to retrieve an employee and his/her todo list progress
"""
if __name__ == "__main__":
    import requests
    import sys

    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user_url = base_url + "users/{}".format(user_id)
    todos_url = base_url + "todos?userId={}".format(user_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    fullname = user.get("name")
    count = 0
    total = len(todos)

    tasks = ""

    for todo in todos:
        if todo.get("completed"):
            count += 1
            title = todo.get("title")
            tasks += "\t {}\n".format(title)

            heading = "Employee {} is done with tasks({}/{}):".format(fullname,
                                                                      count,
                                                                      total)
    print(heading)
    print(tasks, end="")
