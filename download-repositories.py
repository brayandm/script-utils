import requests
import os

# Username of the person whose repositories you want to clone
target_user = 'brayandm'

# Destination path where the cloned repositories will be saved
destination_path = ''

def clone_repositories():
    # Get the list of public repositories for the user
    url = f'https://api.github.com/users/{target_user}/repos'
    response = requests.get(url)
    repos = response.json()

    # Create the destination path if it doesn't exist
    if destination_path != '':
        os.makedirs(destination_path, exist_ok=True)
        os.chdir(destination_path)

    # Clone each repository to the destination path
    for repo in repos:
        os.system(f'git clone {repo["clone_url"]}')

    print('Cloning complete.')

# Execute the repository cloning function
clone_repositories()
