import instaloader
import send_email
from os import environ


def get_loader(login: str, password: str):
    loader = instaloader.Instaloader()
    loader.login(login, password)
    return loader


def get_profile(username: str, loader):
    profile = instaloader.Profile.from_username(loader.context, username)
    return profile


def get_following(profile):
    following = []
    for following_user in profile.get_followees():
        following.append(following_user)
    return following


def get_followers(profile):
    followers = []
    for follower in profile.get_followers():
        followers.append(follower)
    return followers


def get_unfollowers(followers: list, following: list):
    unfollowers = []
    for following in following:
        if following not in followers:
            unfollowers.append(following)
    return unfollowers


def main():
    loader = get_loader(environ['LOGIN'], environ['PASSWORD'])
    profile = get_profile(environ['LOGIN'], loader)
    last_unfollowers = get_unfollowers(get_followers(profile), get_following(profile))
    last_unfollowers_length = len(last_unfollowers)
    while True:
        unfollowers = get_unfollowers(get_followers(profile), get_following(profile))
        if last_unfollowers_length < len(unfollowers):
            for unfollower in unfollowers:
                if unfollower not in last_unfollowers:
                    send_email.send_email(str(unfollower))


if __name__ == '__main__':
    main()
