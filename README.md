GitHub Starred Repos Pull Requests Tracker
About

The GitHub Starred Repos Pull Requests Tracker is a tool designed for developers who want to stay updated with the activity in the repositories they've starred. It provides an efficient way to track all the open pull requests across your starred repositories and also keeps a record of the last 5 closed pull requests from each repository. This tool is perfect for developers who want to keep an eye on projects they're interested in but might not have the time to check each one regularly.
Features

    Live View of Open Pull Requests: Fetch and display a live view of all the open pull requests across your starred GitHub repositories in a markdown file.
    Historical Data of Closed Pull Requests: Along with open pull requests, get a snapshot of the last 5 closed pull requests from each starred repository.
    Delta Updates on New Pull Requests: Re-run the script to generate a new markdown file with just the new open pull requests since the last execution, allowing for efficient tracking over time.
    Easy Integration: Simple setup and execution process, making it easy to integrate into your daily or weekly workflow.
    Markdown Output: All data is stored in markdown files (pull_requests_summary.md and new_pull_requests.md), making it easy to view, share, and store.

Getting Started
Prerequisites

    Python 3.6 or higher
    pip for installing dependencies
    A GitHub Personal Access Token with permissions to read your starred repositories

Installation

    Clone this repository to your local machine:

bash

git clone https://github.com/yourusername/github-starred-pr-tracker.git
cd github-starred-pr-tracker

    Install the required Python dependencies:

bash

pip install -r requirements.txt

    Create a .env file in the root directory of the project and add your GitHub Personal Access Token:

plaintext

GITHUB_TOKEN=your_personal_access_token_here

Usage

    To fetch and view the open and recently closed pull requests in your starred repositories, run:

bash

python track_pull_requests.py

This command generates a pull_requests_summary.md file in the root directory, listing all open pull requests and the last 5 closed pull requests from each starred repository.

    To get a delta view of new open pull requests since the last run, simply re-run the script:

bash

python track_pull_requests.py

Now, a new file new_pull_requests.md will be created, showing only the new open pull requests since the last execution.
Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please feel free to fork the repository, make changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
License

Distributed under the MIT License. See LICENSE for more information.
