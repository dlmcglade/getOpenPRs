import requests
import os  # Import the os module

# Get the GITHUB_TOKEN from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
STARRED_REPOS_URL = "https://api.github.com/user/starred"

def get_pull_requests(repo, state, per_page=100):
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    pulls_url = f"https://api.github.com/repos/{repo}/pulls?state={state}&per_page={per_page}&sort=updated"
    response = requests.get(pulls_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_starred_repositories():
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    starred_repos = []
    page = 1
    while True:
        response = requests.get(f"{STARRED_REPOS_URL}?page={page}", headers=headers)
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        starred_repos.extend(data)
        page += 1
    return [repo['full_name'] for repo in starred_repos]

def main():
    starred_repos = get_starred_repositories()
    summary_content = ""
    new_pull_requests_content = ""
    existing_pulls = set()

    try:
        with open("pull_requests_summary.md", "r") as file:
            for line in file:
                if line.startswith("- **PR #"):
                    existing_pulls.add(line.strip())
    except FileNotFoundError:
        pass

    for repo in starred_repos:
        summary_content += f"## {repo}\n\n"
        open_pulls = get_pull_requests(repo, "open")
        if open_pulls:
            summary_content += "### Open Pull Requests\n"
            for pull in open_pulls:
                pull_line = f"- **PR #{pull['number']}**: {pull['title']} (by {pull['user']['login']}) - [Link]({pull['html_url']})\n"
                summary_content += pull_line
                if pull_line.strip() not in existing_pulls:
                    new_pull_requests_content += pull_line
            summary_content += "\n"
        else:
            summary_content += "No open pull requests.\n\n"

    # Always update pull_requests_summary.md
    with open("pull_requests_summary.md", "w") as file:
        file.write(summary_content)

    # Update new_pull_requests.md only if there are new pull requests
    if new_pull_requests_content:
        with open("new_pull_requests.md", "w") as file:
            file.write(new_pull_requests_content)
        print("New pull requests found and written to new_pull_requests.md. Here are the details:")
        print(new_pull_requests_content)
    else:
        print("No new pull requests to report since the last run.")

if __name__ == "__main__":
    main()
