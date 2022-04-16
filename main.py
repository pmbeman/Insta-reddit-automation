import praw
import subprocess
from instabot import Bot
import time

# Needed variables
ig_username = ""
ig_password = ""
reddit_client_id = ""
reddit_client_secret = ""
user_agent = ""  
sub_reddit = ""

# Instabot instance
bot =  Bot()
bot.login(username=ig_username,password=ig_password)

# Reddit API 
reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent=user_agent,
    )

subreddit = reddit.subreddit(sub_reddit)
a = 0
while True:
    f = open("tags.txt", "r")
    tags = f.read()
    f.close
    
    # Get URL and title of the subreddit
    for submission in subreddit.new(limit=1):
        post_url = str(submission.url)
        title = submission.title

        # Extension of the URL
        extension = ""
        if post_url.endswith(".jpg"):
            extension = ".jpg"
        elif post_url.endswith(".gif"):
            extension = ".gif"
        elif post_url.endswith(".mp4"):
            extension = ".mp4"
        elif post_url.endswith(".png"):
            extension == ".png"
        else:
            print("Extension not set")
            continue
        
        media_name = 'image' + str(a) + extension
        caption = title + "\n\n\n" + tags

        # Download the media from the URL
        subprocess.run('youtube-dl '+ post_url + ' --output "posts/'+ media_name + '"' , shell=True, check=True, capture_output=True)
        
        # media upload
        if extension == ".jpg" or extension == ".png":
            bot.upload_photo(photo="posts/" + media_name, caption=caption)
        elif extension == ".mp4" or extension == ".gif":
            bot.upload_video(video="posts/" + media_name, caption=caption)
        else:
            continue
        
        time.sleep()
    a = a+1
    
