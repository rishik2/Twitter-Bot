import tweepy
import time

consumer_key = '3LbhIolwXUUZPiRTR9okVfo1k'
consumer_secret = 'bQMuIQa1y4bQuhRjn3B5ulH0gdrfrCxfqAzEqcYoBFRIkugu4K'
key = '1429350004943065089-hIAC68H77KAAHU4rh2ofnkFBmbL11Q'
secret = 'LL6veJbobNf1DqIpx46yy6gZV72ysCzQUFcFBbK4VywSV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

# defining the hashtage to be searched
api = tweepy.API(auth)
hashtag = ("#python", '#100daysofcoding', '#java')
tweetnumber = 3
tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

def retweet_hashtag():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Successfull")
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(10)

retweet_hashtag()
