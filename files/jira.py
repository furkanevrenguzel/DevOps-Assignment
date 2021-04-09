import requests
import json
import os.path

config_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.json')

with open(config_file) as config_file:
    config = json.load(config_file)
    auth = (config["jira"]["username"], config["jira"]["password"])


def getProjects():
    url = "http://localhost:8080/JIRA/rest/api/2/project?expand=description"

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()

        if len(json.loads(response.text)) == 0:
            raise SystemExit("No project!")

        return json.loads(response.text)

    except requests.exceptions.RequestException as err:
        raise SystemExit(err)
