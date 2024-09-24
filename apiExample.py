import requests

username = "Devansh0012"

url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"{username} has {len(data)} public repositories")
    
    for repo in data:
        print(f"Repo: {repo['name']}")
        
else:
    print(f"Error: {response.status_code}")
    print(response.json())
    

    