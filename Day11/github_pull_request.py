import requests

def get_commits_details(repo_url):
    try:
        # Make the API request
        response = requests.get(repo_url)

        # Check if the request was successful (status code 200)
        response.raise_for_status()
        
        # Parse JSON response
        complete_details = response.json()

        # Display commit details
        for commit in complete_details:
            committer_id = commit["committer"]["id"]
            committer_login = commit["committer"]["login"]
            print(f'Committer ID: {committer_id}, Committer Login: {committer_login}')

    except requests.exceptions.RequestException as e:
        # Handle any HTTP request errors
        print(f"Error in the API request: {e}")

if __name__ == "__main__":
    # Define the GitHub repository URL
    repo_url = "https://api.github.com/repos/kubernetes/kubernetes/commits"

    # Call the function to get and print commit details
    get_commits_details(repo_url)
