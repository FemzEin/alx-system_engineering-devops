#!/usr/bin/python3
"""
Script to retrieve an employee and his/her todo list progress
"""
if __name__ == "__main__":
    import requests
    import json
    from collections import OrderedDict

    base_url = "https://jsonplaceholder.typicode.com/"
    users_url = base_url + "users"
    users = requests.get(users_url).json()

    filename = "todo_all_employees.json"
    with open(filename, 'w') as f:
        json_users = OrderedDict()
        for user in users:
            user_id = user.get("id")
            username = user.get("username")

            todos_url = base_url + "todos?userId={}".format(user_id)
            todos = requests.get(todos_url).json()

            json_todos = []

            for todo in todos:
                title = todo.get("title")
                completed = todo.get("completed")
                todo_dict = [("username", username),
                             ("task", title),
                             ("completed", completed)]
                todo_dict = OrderedDict(todo_dict)
                json_todos.append(todo_dict)

            json_users[str(user_id)] = json_todos

        json.dump(json_users, f)
