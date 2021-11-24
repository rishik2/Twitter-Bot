import tweepy
import time


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)



FILENAME = 'last_seen_id.txt'

def last_seen_id(FILENAME):
    read_file = open(FILENAME, 'r' )
    last_seen_id = int(read_file.read().strip())
    read_file.close()
    return last_seen_id

def store_last_seen(FILENAME, last_seen_id):
    write_file = open(FILENAME, 'w')
    write_file.write(str(last_seen_id))
    write_file.close()




def reply():
    tweets = api.mentions_timeline(last_seen_id(FILENAME), tweet_mode="extended")
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("Replied to tweet id: "  +  str(tweet.id))
            api.update_status( '@' + tweet.user.screen_name +  " Thanks #100 Days of Coding " + str(tweet.id),  tweet.id )
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILENAME ,tweet.id)
        
while True:    
    reply()
    time.sleep(120)
    print("Working...")

    
            
