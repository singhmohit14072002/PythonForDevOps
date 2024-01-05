# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://capcool1813.atlassian.net/rest/api/3/issue"
API_TOKEN = "ATATT3xFfGF01ArXgZqWbL9Rhjci0KWyQ6abRhZMpOXGkf8tSYoDXN1rXnj4r1REEHWkeFYIZ54WrumtYuzLeCsibxYW6S-Bvf-8TMeWNZON80ySfOV5aKdXcgoGKBKKn5z6HYIVqZP2Eg9VdDfj4n0KU7TZAuuI7xOAQI6iCeWD2klCw27kiQw=E460D3B3"
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
      "key": "KAN"
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

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))