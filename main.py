import os
import git
from github import Github

# Set up environment variables or constants
GITHUB_TOKEN = os.getenv('AUTO_PUSH_GITHUB_TOKEN')  # Load token from environment
REPO_URL = 'https://github.com/meharsarmad786/autogit.git'
LOCAL_REPO_PATH = '/Users/app/Downloads/AutoGithub'  # Use the full path here
COMMIT_MESSAGE = 'Automated commit and push'

def push_to_github():
    try:
        # Initialize Git repository if not already initialized
        if not os.path.exists(os.path.join(LOCAL_REPO_PATH, '.git')):
            print(f"Repository not initialized at {LOCAL_REPO_PATH}. Cloning...")
            git.Repo.clone_from(REPO_URL, LOCAL_REPO_PATH)
        
        repo = git.Repo(LOCAL_REPO_PATH)

        # Pull latest changes from remote to avoid conflicts
        origin = repo.remote(name='origin')
        origin.pull()

        # Check for changes and commit them
        if repo.is_dirty(untracked_files=True):
            print("Changes detected. Staging and committing...")
            repo.git.add(A=True)  # Add all changes (including untracked files)
            repo.index.commit(COMMIT_MESSAGE)

            # Push changes to GitHub
            origin.push()
            print("Changes pushed to GitHub successfully.")
        else:
            print("No changes to push.")
    except git.exc.GitCommandError as e:
        print(f"Git command failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def create_github_repo(repo_name):
    try:
        # Authenticate with GitHub API
        if not GITHUB_TOKEN:
            print("GitHub token is not set. Please export 'AUTO_PUSH_GITHUB_TOKEN'.")
            return
        
        g = Github(GITHUB_TOKEN)
        user = g.get_user()
        
        # Create a private GitHub repository
        repo = user.create_repo(repo_name, private=True)
        print(f"Repository '{repo_name}' created successfully.")
        return repo.clone_url
    except Exception as e:
        print(f"Error during GitHub repository creation: {e}")

if __name__ == '__main__':
    # Example: Push changes to an existing repository
    push_to_github()

    # Example: Create a new repository and push
    # new_repo_url = create_github_repo('Auto_Github1')
    # print(f"New repo URL: {new_repo_url}")
