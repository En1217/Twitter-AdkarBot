import tweepy

"""
مفاتيح تويتر غير الاكس للمفاتيح حقت حسابك
تقدر تجيب مفاتيح لحسابك بتويتر من هنا
developer.twitter.com 
"""    
consumer_key = "DIeWhSGKLsIb6ax79GxprqbYjQ5G4Te9owPkJUD19Oh9J"
consumer_secret = "DIeWhSGKLsIb6ax79GxprqbYjQ5G4Te9owPkJUD19Oh9J"
access_token= "820412749243121665-EqYMr17br3TFTesqMcmwqNwL8PtSY4P"
access_secret = "DIeWhSGKLsIb6ax79GxprqbYjQ5G4Te9owPkJUD19Oh9J"

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
