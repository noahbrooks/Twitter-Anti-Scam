import tweepy
import time

# Authentication + Keys
## Removed my information, but you would get the below information from Twitter
## When you sign up for access to their API
consumer_key = ''
consumer_secret = ''
key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

# API Object

api = tweepy.API(auth)

## File that stores last seen tweet by its ID
## Each Tweet has a unique ID that will go in order
## So if it's a higher number, you know it is a newer Tweet
FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

query = 'put whatever youre searching for here'

tweets = api.search(q=query,since_id=read_last_seen(FILE_NAME))

def reply():
    for tweet in reversed(tweets):
            if query in tweet.text.lower():
                print(str(tweet.id) + ' - ' + tweet.text)
                api.update_status(tweet.text.split()[0] + " " + tweet.user.name + " testing ", tweet.id)
                store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)
