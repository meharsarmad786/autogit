import os
import git
from github import Github

# Set up environment variables or constants
GITHUB_TOKEN = os.getenv('AUTO_PUSH_GITHUB_TOKEN')  # Load token from environment
REPO_URL = 'https://github.com/AwaisSabit/repository.git'
LOCAL_REPO_PATH = r"C:\Users\Awais Sabit\Desktop\projects\AutoGithub"
COMMIT_MESSAGE = 'Automated commit and push'

def push_to_github():
    try:
        # Initialize Git repository
        repo = git.Repo(LOCAL_REPO_PATH)
        if repo.is_dirty(untracked_files=True):
            # Stage all changes
            repo.git.add(A=True)
            # Commit changes
            repo.index.commit(COMMIT_MESSAGE)
            # Push changes
            origin = repo.remote(name='origin')
            origin.push()
            print("Changes pushed to GitHub successfully.")
        else:
            print("No changes to push.")
    except Exception as e:
        print(f"Error during Git operation: {e}")

def create_github_repo(repo_name):
    try:
        # Authenticate with GitHub API
        g = Github(GITHUB_TOKEN)
        user = g.get_user()
        repo = user.create_repo(repo_name)
        print(f"Repository '{repo_name}' created successfully.")
        return repo.clone_url
    except Exception as e:
        print(f"Error during GitHub repository creation: {e}")

if __name__ == '__main__':
    # Example: Push changes to an existing repository
    push_to_github()

    # Example: Create a new repository and push
    # new_repo_url = create_github_repo('Auto_Github')
    # print(f"New repo URL: {new_repo_url}")
