# GitHub Starred Repos Pull Requests Tracker

GetOpenPRs is designed for developers who want to stay updated with the activity in the repositories they've starred. It provides an efficient way to track all the open pull requests across your starred repositories and also keeps a record of the last 5 closed pull requests from each repository. This tool is perfect for developers who want to keep an eye on projects they're interested in but might not have the time to check each one regularly.

## Features

- **Live View of Open Pull Requests**: Fetch and display a live view of all the open pull requests across your starred GitHub repositories in a markdown file.
- **Historical Data of Closed Pull Requests**: Along with open pull requests, get a snapshot of the last 5 closed pull requests from each starred repository.
- **Delta Updates on New Pull Requests**: Re-run the script to generate a new markdown file with just the new open pull requests since the last execution, allowing for efficient tracking over time.
- **Easy Integration**: Simple setup and execution process, making it easy to integrate into your daily or weekly workflow.
- **Markdown Output**: All data is stored in markdown files (`pull_requests_summary.md` and `new_pull_requests.md`), making it easy to view, share, and store.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `pip` for installing dependencies (if we get around to doing any)
- A GitHub Personal Access Token with permissions to read your starred repositories

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/dlmcglade/getOpenPRs.git
cd getOpenPRs
```

2. Setup

getOpenPRs.py uses GITHUB_TOKEN stored as an environment variable

```bash
export GITHUB_TOKEN="YOUR_PERSONAL_ACCESS_TOKEN"
```


3. Running

```bash
python3 getOpenPRs.py
```
