import keys
import tweepy

auth=tweepy.OAuthHandler(keys.consumer_key,keys.consumer_secret)

auth.set_access_token(keys.access_token,keys.access_token_secret)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user=api.get_user("Nasa")

#print(user.name)
#print(user.description)
#print(user.status.text)
#print(user.followers_count)
#print(user.friends_count)

me=api.me()
#print(me)

followers=[]
cursor=tweepy.Cursor(api.followers,screen_name='ericakaze')
for account in cursor.items(10):
    followers.append(account.screen_name)
#print(followers)
print('Followers:',', '.join(sorted(followers,key=lambda s:s.lower())))

friends=[]
cursor=tweepy.Cursor(api.friends,screen_name='ericakaze')
for account in cursor.items(10):
    friends.append(account.screen_name)
#print(friends)
print('Friends:',', '.join(sorted(friends)))

tweets=api.user_timeline(screen_name='ericakaze',count=3)
for tweet in tweets:
    print(tweet.text,'\n')