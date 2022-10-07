
import tweepy


# self created script imported for the functions
import database as db
import englishTweets as eSA
import germanTweets as gSA


# Authentication for the Twitter API
consumerKey = '8TG4aUTkflUUJfctNNJg0dSYO'
consumerSecret = 'IBweDvTTgLLONbZnw2RndSCNu51p4Tf738BL3g1HRPC6Y9CVyO'
accessToken = '1517195740380114944-ArUIbOAPPXCnEPPB2xVpiItZWdR1Df'
accessTokenSecret = 'D7Kuxk8jbrQkzY3bDHq8KHb2Qi8zV4sywW4v0GaMtJ52w'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


#LET THE USER DECIDE WHAT THEY WANT TO SEARCH FOR AND HOW MANY TWEETS SHOULD BE SCRAPED

keyword = input("Enter keyword or hashtag to analyse: ")
print()
noOfTweets = int(input("Enter the amount of keyword tweets to analyse: "))

#GETTING THE TWEETS WITH TEEPY (Langauges: English -> en, German -> de)
language = input("Enter the language of tweets: ")
language = language.lower()
print(language)


# q = keyword -> user specified keyword to search for
# lang -> language to search for
# tweet_mode = 'extended' -> gets the entire tweet [without it, tweet gets truncated at 140 characters]
# noOfTweets -> user specified amount of tweets to search for

if language =='en':
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang='en', tweet_mode='extended').items(noOfTweets)

if language =='de':
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang='de',tweet_mode='extended').items(noOfTweets)


# * translatedToEnglish_list -> This is the list containing the English translation tweets
# * translatedToGerman_list -> This is the list containing the German translation tweets
# * originalGerman_list -> A list of  German tweets
# * originalEnglish_list -> A list of  German tweets



if language == 'en':

    originalEnglish_list, translatedToGerman_list= eSA.englishTweets(tweets)

if language == 'de':
    
    originalGerman_list, translatedToEnglish_list = gSA.germanTweets(tweets)

  
# print("================================== ADD TO DATABASE ============================")

if language == 'en':
    print("====== ADDING TO DATABASE ======")
    
    # inserts  English tweets into  English database
    for tweet in originalEnglish_list:
        db.addIntoDatabaseENGLISH(tweet)
    
    # insert  German translation into germantranslation  database
    for tweet in translatedToGerman_list:
        db.addIntoDatabaseGERMAN_TRANSLATION(tweet)
    
        

if language == 'de':
    print("====== ADDING TO DATABASE ======")

    # inserts  German tweets into  German database
    for tweet in originalGerman_list:
        db.addIntoDatabaseGERMAN(tweet)
   
    # insert original English translation into englishtranslation  database
    for tweet in translatedToEnglish_list:
        db.addIntoDatabaseENGLISH_TRANSLATION(tweet)

    
print("====== FINISHED ======")
