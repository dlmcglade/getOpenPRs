Keep track of all the github repos you have *starred* by fetching a live view of all the open pull requests in markdown. Run the script again for the latest delta on just the new pull requests since the last run.

--

Reads all repos you have *starred* and creates a list of all open pull requests and the last 5 closed pull requests from each repo and stores in markdown file (pull_requests_summary.md).

Upon re-running script, a new markdown file (new_pull_requests.md) is created with just the open pull requests that are new since you last ran the script.

Each subsequent re-run of the script performs the same, but only displays the newest open pull requests since the last run.
