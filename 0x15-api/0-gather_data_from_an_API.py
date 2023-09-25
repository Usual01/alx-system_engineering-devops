#!/usr/bin/python3
""" using a REST API for a given employee ID
    returns information about his/her TODO list progress
    accept an integer as a parameter (employee ID)

"""
import json
import requests
import sys

if __name__ == "__main__":
    """ concatinating url with query strings
        request the page
        json.loads to convert json to python dictionary
    """

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # User detail
    user = requests.get(url + "users/{}".format(user_id)).json()

    # request all todo list of the ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # completed todo task
    todo_completed = requests.get(url + "todos",
                                  params={"userId": user_id,
                                          "completed": "true"}
                                  ).json()

    print("Employee {} is done with tasks({}/{}):"
          .format(user["name"], len(todo_completed), len(todos)))
    # loop through to display each task title
    for task in todo_completed:
        print("\t {}".format(task["title"]))
