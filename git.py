import subprocess
import os
import datetime

def git_push():
    try:
        # Configure Git (only needs to be done once)
        subprocess.run(["git", "config", "--global", "user.email", "mahersarmad786@gmail.com"], check=True)
        subprocess.run(["git", "config", "--global", "user.name", "meharsarmad786"], check=True)

        # Make changes (example: add timestamp to a file)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("timestamp.txt", "a") as f:
            f.write(f"Updated at: {timestamp}\n")

        # Add, commit, and push
        subprocess.run(["git", "add", "."], check=True)
        try:
          subprocess.run(["git", "commit", "-m", "Automated commit from local script"], check=True)
        except subprocess.CalledProcessError as e:
          if "nothing to commit" in e.stderr.decode():
              print("No changes to commit.")
              return
          else:
              raise # Re-raise other errors
        subprocess.run(["git", "push"], check=True)

        print("Changes pushed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error pushing changes: {e}")
        if e.stderr:
            print(f"Stderr: {e.stderr.decode()}")
    except FileNotFoundError:
        print("Git command not found. Make sure Git is installed and in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Check if we are in a Git repository
    if os.path.exists(".git"):
        git_push()
    else:
        print("Not a Git repository. Please run this script in a Git repository directory.")