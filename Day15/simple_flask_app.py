from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
# creating a flask app instance 
app = Flask("__name__")

@app.route("/createJIRA", methods=["POST"]) 
def createJIRA():
    url = "https://capcool1813.atlassian.net/rest/api/3/issue"
    API_TOKEN = "ATATT3xFfGF0KBY-Nec58skZ_QK_b87IVHbyXIohHFRBa0ficxhvILr1pEkT3YpVZ4mzP8hPFSeIjHtjHgGFKXEb6NW2UqtZ7GLaaJ5ao142GO0AShQnq0hlr6Pu77snlQKwicFURChNJ_g-j-4b1ssRDY76c_N1zyjIEfDDrQdbJhmCs9yFAYI=9050BE39"
    auth = HTTPBasicAuth("capcool1813@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
            {
                "content": [
                {
                    "text": "My First Jira Ticket",
                    "type": "text"
                }
                ],
                "type": "paragraph"
            }
            ],
            "type": "doc",
            "version": 1
        },
        "issuetype": {
            "id": "10005"
        },
        "labels": [
            "bugfix",
            "blitz_test"
        ],
        "project": {
            "key": "MOH"
        },
        "summary": "First Jira Ticket",
        },
        "update": {}
    } )

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


    #flask come with cevelopment server
app.run('0.0.0.0', port=5000)









