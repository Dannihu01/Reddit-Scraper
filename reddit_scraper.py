#! usr/bin/env python3

import praw
import pandas as pd 
import datetime as dt

reddit_wrap = praw.Reddit(client_id='fqqAzLDxlZ86-A', \
                            client_secret='GCtXSXE0V4eMZvY9GMHipmvwgNg',\
                                user_agent = 'Reddit_Scraper')



subreddit = reddit_wrap.subreddit('EDM')

top_subreddit = subreddit.hot(limit = 100)



topics_dict = {
    "title":[],\
            "url":[],\
                "body":[], 
                    "created":[]
}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["url"].append(submission.url)
    topics_dict["body"].append(submission.selftext)
    topics_dict["created"].append(submission.created)


topics_data = pd.DataFrame(topics_dict)

def get_date(created):
    return dt.datetime.fromtimestamp(created)


_timestamp = topics_data["created"].apply(get_date)

topics_data = topics_data.assign(timestamp = _timestamp)


topics_data.to_csv('Reddit_Scraper.csv', index=False)