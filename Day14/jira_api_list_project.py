import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://capcool1813.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF01ArXgZqWbL9Rhjci0KWyQ6abRhZMpOXGkf8tSYoDXN1rXnj4r1REEHWkeFYIZ54WrumtYuzLeCsibxYW6S-Bvf-8TMeWNZON80ySfOV5aKdXcgoGKBKKn5z6HYIVqZP2Eg9VdDfj4n0KU7TZAuuI7xOAQI6iCeWD2klCw27kiQw=E460D3B3"

auth = HTTPBasicAuth("capcool1813@gmail.com", API_TOKEN)

headers = {
    "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)

output = json.loads(response.text)

# Use a for loop to iterate over the projects and print their names
for project in output:
    name = project["name"]
    print(name)
