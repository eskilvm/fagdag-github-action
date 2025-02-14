from github import PullRequest, InputGitAuthor, Repository

def get_latest_commit_message(pull_request : PullRequest) -> list[str]:
    return [c.commit.message for c in pull_request.get_commits()][-1]        

def commit_and_push(repo: Repository, target_branch:str, file_path: str) -> None:
    author = InputGitAuthor(
    "GitHub Action",
    "action@github.com")
    commit_message = f"Add haiku art"
    with open(file_path) as f: new_file_content = f.read()
    remote_file = repo.get_contents(file_path, ref=target_branch)
    
    repo.update_file(
        remote_file.path,
        commit_message,
        new_file_content,
        remote_file.sha,
        branch = target_branch,

        author = author)
