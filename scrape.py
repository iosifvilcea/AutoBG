from __future__ import print_function
import re, praw, requests, os, glob, sys
from bs4 import BeautifulSoup

# ****************************************************
#   Get Top
# ****************************************************
def get_top():
    r = praw.Reddit(user_agent="iv-Scrape v0.0")
    submissions = r.get_subreddit(sys.argv[1]).get_top(limit=5)

    for submission in submissions:
        
        if 'http://i.imgur.com/' in submission.url:
            imageUrl = submission.url
            
            #Gets rid of the ?1 some imgur links have.
            if '?' in imageUrl:
                imageUrl = imageUrl[:imageUrl.find('?')]
          
            #Get image id and extension.
            # Set it as fileName.
            fileName = imageUrl.split('/')
            downloadImage(imageUrl , fileName[3])

        #If its just a direct image link, just download it.
        elif '.png' or '.jpeg' or '.jpg' in submission.url:
            fileName = imageUrl.split('/')
            downloadImage(imageUrl, fileName[3])

        else:
            print("wut? ", submission.url)

# ****************************************************
#   Download Image
#    param: ImageUrl - image link
#           fileName - name of file to be saved
# ****************************************************
def downloadImage(imageUrl , fileName):
    response = requests.get(imageUrl, stream=True)
    
    if response.status_code == 200:
        print('Downloading ', imageUrl, ' ...')
        with open(fileName, 'wb') as fd:
            for chunk in response.iter_content(4096):
                fd.write(chunk)


# ****************************************************
#   Main
# ****************************************************
if __name__ == "__main__":
    
    MIN_SCORE = 100
    if len(sys.argv) < 2:
        print("Usage: python scrape.py [subreddit] ")
        sys.exit()
    elif len(sys.argv) > 2:
        print('Error: Too many arguments.')
        sys.exit()

    #Download top reddit posts.
    get_top()
