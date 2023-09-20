import json
import os
from instagrapi import Client
from shutil import move

# Load credentials
with open("config/credentials.json", "r") as file:
    credentials = json.load(file)

# Authenticate with Instagram
cl = Client()
cl.login(credentials["username"], credentials["password"])

# Iterate over files in the posts directory and post them
for post_file in os.listdir("posts/"):
    post_path = os.path.join("posts", post_file)
    
    # For this example, we're assuming images. If videos, use cl.video_upload().
    media = cl.photo_upload(post_path, caption="Automated post using instagrapi!")
    
    # Move posted image to 'published' folder to prevent reposting
    move(post_path, os.path.join("published", post_file))

print("Done posting!")

# dm function
def send_dm(username, message):
    client = Client()
    client.login("YOUR_USERNAME", "YOUR_PASSWORD")  # Use your own credentials or fetch from a config file

    user_id = client.user_id_from_username(username)
    client.direct_send(message, [user_id])
    
# follow function   
def follow_user(username):
    client = Client()
    client.login("YOUR_USERNAME", "YOUR_PASSWORD")

    user_id = client.user_id_from_username(username)
    client.user_follow(user_id)
