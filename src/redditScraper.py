import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent="ratem/0.1 by tkofb"
)

username = "spez" 
redditor = reddit.redditor(username)

# Can also be .top() or .hot() [Think about what you prefer]
for post in redditor.submissions.new(limit=10):
    print(f"Title: {post.title}")
    print(f"Subreddit: {post.subreddit}")
    print(f"Score: {post.score}")
    print(f"URL: {post.url}")
    print("-" * 40)

