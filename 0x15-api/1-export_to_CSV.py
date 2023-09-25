#!/usr/bin/python3
"""
    exporting the data requested to CSV
"""
if __name__ == "__main__":
    """converts json to python dictionary
    export to csv file
    Format:
        "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    """
    import csv
    import io
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
    with open("{}.csv".format(user_id), 'w', newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([user_id, username, t.get("completed"),
                            t.get("title")])
