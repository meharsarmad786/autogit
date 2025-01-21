# from dotenv import load_dotenv
import os

# load_dotenv()

token = os.getenv("AUTO_PUSH_GITHUB_TOKEN")
# print(os.environ)
if token:
    print("Success")
else:
    print('None')
