#!/usr/bin/python3
"""
    exporting the todo list data of a given employee ID to JSON format
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # User detail
    user = requests.get(url + "users/{}".format(user_id)).json()

    # request all todo list of the ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    username = user.get("username")

    # writing newly created py dictionary into a csv file
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)
