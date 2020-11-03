from instabot import Bot
from time import sleep
import send_email
from os import environ


def get_following():
    following_list = []
    bot = Bot()
    bot.login(username=environ['LOGIN'], password=environ['PASSWORD'])
    following = bot.get_user_following(environ['LOGIN'])
    for flwing in following:
        following_list.append(bot.get_username_from_user_id(flwing))
    return following_list


def get_followers():
    followers_list = []
    bot = Bot()
    bot.login(username=environ['LOGIN'], password=environ['PASSWORD'])
    followers = bot.get_user_followers(environ['LOGIN'])
    for follower in followers:
        followers_list.append(bot.get_username_from_user_id(follower))
    return followers_list


def get_unfollowers(followers: list, following: list):
    unfollowers = []
    for following in following:
        if following not in followers:
            unfollowers.append(following)
    return unfollowers


def main():
    last_unfollowers = get_unfollowers(get_followers(), get_following())
    last_unfollowers_length = len(last_unfollowers)
    while True:
        unfollowers = get_unfollowers(get_followers(), get_following())
        if last_unfollowers_length < len(unfollowers):
            for unfollower in unfollowers:
                if unfollower not in last_unfollowers:
                    send_email.send_email(str(unfollower))
        print('Sleeping for 5 minutes.')
        sleep(300)


if __name__ == '__main__':
    main()
