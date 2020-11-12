import instaloader
import secrets
import send_email
from time import sleep


def login_loader(username: str, password: str):
    loader = instaloader.Instaloader()
    loader.login(username, password)
    return loader


def get_profile(username: str, loader):
    profile = instaloader.Profile.from_username(loader.context, username)
    return profile


def get_followers(profile):
    followers = []
    for follower in profile.get_followers():
        followers.append(follower.username)
    return followers


def main():
    last_profile = get_profile(secrets.LOGIN, login_loader(secrets.LOGIN, secrets.PASSWORD))
    last_followers = get_followers(last_profile)
    while True:
        profile = get_profile(secrets.LOGIN, login_loader(secrets.LOGIN, secrets.PASSWORD))
        followers = get_followers(profile)
        if len(last_followers) > len(followers):
            for follower in followers:
                if follower not in last_followers:
                    send_email.send_email(follower)
        last_followers = followers
        print('Sleeping for 5 minutes')
        sleep(300)

if __name__ == '__main__':
    main()
