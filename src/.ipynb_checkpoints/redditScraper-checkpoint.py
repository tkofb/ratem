import praw
import os
from dotenv import load_dotenv
from tickers.processTickers import getTickers
import pandas as pd
from datetime import datetime, UTC


# This is to ignore the praw warning. Try it later to make sure it is the only deprecated package
load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent="ratem/0.1 by tkofb"
)

# jsw5224
# username = input("What user would you like to rate: ") 
username = 'jsw5224'
redditor = reddit.redditor(username)

tickers = getTickers()
tickerSet = set(tickers['Symbol'])

stocks = pd.DataFrame(columns=['Symbol', 'Start Date', 'End Date'])
stocksLen = 0
print(stocks)

# Can also be .top() or .hot() [Think about what you prefer]
for post in redditor.submissions.new(limit=10):
    # Want to focus only on penny stocks subreddit for now
    # post_date = datetime.utcfromtimestamp(post.created_utc)
    post_date = datetime.fromtimestamp(post.created_utc, UTC)
    
    if post.subreddit == 'pennystocks':
        
        print(f"Title: {post.title}")
        if post.is_self:
            currPost = post.selftext
            currPostSet = set(currPost.split())

            for elem in currPostSet:
                if elem in tickerSet:
                    stocks.loc[stocksLen] = [elem, post_date, datetime.now(UTC)]
                    stocksLen += 1
                    print(elem)
        else:
            print("This is a link post.")
            print(f"URL: {post.url}")

        # print(f"URL: {post.url}")
        print("-" * 40)
        
print("_" * 40)
print(stocks.head())

