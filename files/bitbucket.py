import requests
import json
import os.path


config_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.json')


with open(config_file) as config_file:
    config = json.load(config_file)
    auth = (config["bitbucket"]["username"], config["bitbucket"]["password"])


def addProject(key, name, description):
    url = "http://localhost:7990/Bitbucket/rest/api/1.0/projects"

    json_data = {}
    json_data["key"] = key
    json_data["name"] = name
    json_data["description"] = description
    data = json.dumps(json_data)

    headers = {
        'Content-Type': "application/json"
    }

    try:
        response = requests.post(url, auth=auth, headers=headers, data=data)
        response.raise_for_status()
        print("Success! Name: " +
              name + ", Key: " + key)
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)


def getProjects():
    url = "http://localhost:7990/Bitbucket/rest/api/1.0/projects"

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        return json.loads(response.text)

    except requests.exceptions.RequestException as err:
        raise SystemExit(err)


def isPorjectExist(key, name, projects):
    for project in projects:
        if project["name"] == name and project["key"] == key:
            return True

    return False
