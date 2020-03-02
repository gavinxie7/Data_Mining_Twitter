import keys
import tweepy

auth=tweepy.OAuthHandler(keys.consumer_key,keys.consumer_secret)
auth.set_access_token(keys.access_token,keys.access_token_secret)
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
tweets=api.search(q="#marchmadness",count=3)
#print(tweets)
#for tweet in tweets:
    #print(tweet.user.screen_name,":",tweet.text)

trends_available=api.trends_available()
#print(len(trends_available))
#print(trends_available[:5])
world_trends=api.trends_place(id=2459115)#the id for NYC
#print(world_trends)
trends_list=world_trends[0]["trends"]
#print(trends_list[0])
trends_list=[t for t in trends_list if t["tweet_volume"]]

from operator import itemgetter
trends_list.sort(key=itemgetter("tweet_volume"),reverse=True)

topics={}

for trend in trends_list:
    topics[trend["name"]]=trend["tweet_volume"]

from wordcloud import WordCloud

wordcloud=WordCloud(
    width=1600,
    height=900,
    prefer_horizontal=0.5,
    min_font_size=10,
    colormap="prism",
    background_color="white",
)
wordcloud=wordcloud.fit_words(topics)
wordcloud=wordcloud.to_file("TrendingTwitter.png")
print("done")