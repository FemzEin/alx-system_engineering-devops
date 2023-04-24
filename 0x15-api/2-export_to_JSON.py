#!/usr/bin/python3
"""
Script to retrieve an employee and his/her todo list progress
"""
if __name__ == "__main__":
    import sys
    import requests
    import json
    from collections import OrderedDict

    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user_url = base_url + "users/{}".format(user_id)
    todos_url = base_url + "todos?userId={}".format(user_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")

    filename = "{}.json".format(user_id)
    with open(filename, 'w') as f:
        json_todos = []
        for todo in todos:
            title = todo.get("title")
            completed = todo.get("completed")
            todo_dict = [("task", title),
                         ("completed", completed),
                         ("username", username)]
            todo_dict = OrderedDict(todo_dict)
            json_todos.append(todo_dict)
        json.dump({str(user_id): json_todos}, f)
