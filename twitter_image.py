import tweepy
import requests
import time


def save_twitter_data(tweet_url, files_location):
    consumer_key = "consumer_key"
    consumer_secret = "consumer_secret"
    access_token = "access_token"
    access_token_secret = "access_token_secret"
    tweet_id = tweet_url.split('?s')[0].split("/")[-1]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    ids = [tweet_id]
    epoc_time = time.time()
    image_name = files_location+ids[0]+str(epoc_time)+'pic.jpg'
    tweets = api.statuses_lookup(ids, include_entities=True, trim_user=True, tweet_mode="extended")
    for tweet in tweets:
        media_url = tweet.extended_entities['media'][0]["media_url"]
        with open(image_name, 'wb') as handle:
            response = requests.get(media_url, stream=True)
            if response.status_code == 200:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
