from instagrapi import Client


def login_to_instagram(username, password):
    client = Client()
    client.login(username, password)
    return client


def fetch_comments(client, media_id):
    comments = client.media_comments(media_id)
    return comments


if __name__ == "__main__":
    USERNAME = "your_username"
    PASSWORD = "your_password"
    MEDIA_ID = "some_media_id"

    client = login_to_instagram(USERNAME, PASSWORD)
    comments = fetch_comments(client, MEDIA_ID)

    for comment in comments:
        print(comment.text)
