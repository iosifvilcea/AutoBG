from __future__ import print_function
import re, praw, requests, os, glob, sys
from bs4 import BeautifulSoup

#url = "https://i.imgur.com/Q6FfWwZ.png"
i = 0

def get_top():
    r = praw.Reddit(user_agent="iv-Scrape v0.0")
    submissions = r.get_subreddit(sys.argv[1]).get_top(limit=5)

    for submission in submissions:
        
        if "imgur.com" not in submission.url:
                continue
        elif 'http://i.imgur.com/' in submission.url:
            fileName = submission.url
            if '?' in fileName:
                fileName = fileName[:fileName.find('?')]

            print("finna get ", fileName)

            downloadImage(fileName)

        else:
            print("wut? ", submission.url)


def downloadImage(imageUrl):
    response = requests.get(imageUrl, stream=True)
    
    if response.status_code == 200:
        print('Downloading ', imageUrl, ' ...')
        fileName = "filename.jpg" 
        with open(fileName, 'wb') as fd:
            for chunk in response.iter_content(4096):
                fd.write(chunk)

if __name__ == "__main__":
    
    MIN_SCORE = 100
    if len(sys.argv) < 2:
        print("Usage: python scrape.py 'subreddit' ")
        sys.exit()
    elif len(sys.argv) > 2:
        print('Error: Too many arguments.')
        sys.exit()

    get_top()
    #printSoup()
