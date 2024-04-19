import tweepy

"""
مفاتيح تويتر غير الاكس للمفاتيح حقت حسابك
تقدر تجيب مفاتيح لحسابك بتويتر من هنا
developer.twitter.com 
"""    
consumer_key = "xxxxxx"
consumer_secret = "xxxxxx"
access_token= "820412749243121665-1SDtPwPZZ3LntWJiEAVIvOd2NJBm8P7"
access_secret = "PMbtKJnUfNePZMTNCt5xtwd5dVJ7WqFFkEMtLXj2JQ1uc"

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
