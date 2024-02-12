# Open Pull Requests Fetcher for Starred Repositories

## Introduction
This Python script retrieves open pull requests for repositories you have starred on GitHub. It's designed to help developers keep track of contributions and updates in projects they are interested in.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
Ensure Python is installed on your system. If not, you can download it from [python.org](https://python.org).

1. Clone or download this script to your local machine.
2. Open a terminal and navigate to the script's directory.
3. Install the required Python packages:

```
pip install requests
```

## Usage
Before running the script, make sure your `GITHUB_TOKEN` environment variable is set, as it's needed to authenticate with the GitHub API and access your starred repositories.

To run the script:

```
python getOpenPRs.py
```

This command will fetch and display open pull requests for your starred repositories.

## Features
- Retrieves open pull requests from the user's starred GitHub repositories.
- Uses GitHub API with proper authentication.
- Easy to use with minimal configuration.

## Dependencies
- Python 3.x
- `requests` library

## Configuration
To use this script, you must have a personal GitHub token set as an environment variable:

```
export GITHUB_TOKEN='your_github_token_here'
```

This token is necessary for the script to authenticate with GitHub and retrieve information about your starred repositories.

## Examples
To see the script in action, simply run it after setting up your GitHub token. No additional arguments are required.

## Troubleshooting
- **Missing GITHUB_TOKEN**: Ensure the `GITHUB_TOKEN` environment variable is correctly set as detailed in the [Configuration](#configuration) section.

## License
This script is provided under the MIT License. See the LICENSE file for more details.
