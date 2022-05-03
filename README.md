# Insta-reddit-automation
A simple script to download posts in the best available format using youtube-dl from a sub reddit and then upload that on instgram.

    python main.py
Enjoy automation :D
# Installation
**1. Clone the repo**

**2. Download all requirements**
  
    pip install -r requirements.txt
**youtube-dl**

You will also need youtube-dl so download it from [here](http://ytdl-org.github.io/youtube-dl/download.html)
and add in ur path.



# Configure the script
**Get client ID and secret.**

Visit [here](https://www.reddit.com/prefs/apps/) to create a reddit app and get the client ID and secret.

Check [this](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html) to learn more about it.

Use this user-agent as an example: `android:com.example.myredditapp:v1.2.3 (by u/<reddit user-name>)`

**Set the needed variables**
* Open main.py and set the variables as required.
  
```python
# Needed variables  
ig_username = ""
ig_password = ""
reddit_client_id = ""
reddit_client_secret = ""
user_agent = ""  
sub_reddit = ""
```
**Tags**

Open tags.txt and type whatever tags u want to display in the caption.
# Extras:
* Delete the /config/ folder evertime you restart the script.

- Click  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/pmbeman/Insta-reddit-automation)
