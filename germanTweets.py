

import pandas as pd
import googleTranslate as gt


"""
Use this to retrieve German tweets, translate them into English, and return seperate lists German and English translation

input: tweets
output: tweet_list, originalGerman_list, translatedToEnglish_list
"""

def germanTweets(tweets):



    originalGerman_list = []
    translatedToEnglish_list = []

    for tweet in tweets:
        #Appending every single tweet to the list

        #if the tweets has a retweet status, return the full_text of the retweeted_status 
        #added benefit that it doesn't include RT @username
        if 'retweeted_status' in tweet._json:
            print("RETWEET")
            tweet_extended = tweet._json['retweeted_status']['full_text']
        else:
            print("NOT RETWEET")
            tweet_extended = tweet.full_text

        #transalting the german tweets into english
        translation = gt.translate_text_with_model('en', tweet_extended, model="nmt")
    
        #adding the translated tweets to the list 'translatedToEnglish'
        translatedToEnglish_list.append(translation)

        #adding the original german tweets to the list 'originalGerman_list'
        originalGerman_list.append(tweet_extended)



    return  originalGerman_list, translatedToEnglish_list
