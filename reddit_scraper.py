#! usr/bin/env python3

import praw
import pandas as pd 
import datetime as dt

reddit_wrap = praw.Reddit(client_id='fqqAzLDxlZ86-A', \
                            client_secret='GCtXSXE0V4eMZvY9GMHipmvwgNg',\
                                user_agent = 'Reddit_Scraper',\
                                    username='NonlinearApplet',\
                                        password = 'tepidbunny2001@')


subreddit = reddit_wrap.subreddit('indieheads')

top_subreddit = subreddit.hot(limit = 100)

for submission in subreddit.hot(limit = 10):
    print(submission.title, submission.id)
    print (' ')

topics_dict = {
    "title":[],\
        "id":[],\
            "url":[],\
                "created":[], \
                    "body":[]
}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)


topics_data = pd.DataFrame(topics_dict)
