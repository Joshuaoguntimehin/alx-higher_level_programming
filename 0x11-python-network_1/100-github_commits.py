#!/usr/bin/python3
"""import statement """
import requests
import sys
"""in a new world"""
def get_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()
    
    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repo> <owner>")
        sys.exit(1)
    
    repo = sys.argv[1]
    owner = sys.argv[2]
    get_commits(repo, owner)
