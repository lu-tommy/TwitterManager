import tweepy
from keys import *
#keys obtained from twitter
API_KEY = API_KEY
API_KEY_SECRET = API_KEY_SECRET
BEARER_TOKEN = BEARER_TOKEN
ACCESS_TOKEN = ACCESS_TOKEN
ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET
CLIENT_ID = CLIENT_ID
CLIENT_SECRET = CLIENT_SECRET
#key handler
def OAuth():
    try:
        auth = tweepy.OAuthHandler(API_KEY,API_KEY_SECRET)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        return auth
    except Exception as e:
        return None
oauth = OAuth()
api=tweepy.API(oauth, parser=tweepy.parsers.JSONParser())
# BEARER_TOKEN
auth1 = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
api2 = tweepy.API(auth1)
client = tweepy.Client(BEARER_TOKEN)

#USA
usa_woeid = 23424977


#send tweet
api.update_status("")
#follow
api.create_friendship("")
#unfollow
api.destroy_friendship("")