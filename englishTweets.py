
import pandas as pd
import googleTranslate as gt

"""
Use this to retrieve English tweets, translate them into German, and return seperate lists English and German translation

input: tweets
output: tweet_list, originalEnglish_list, translatedToGerman_list
"""

def englishTweets(tweets):
    

    originalEnglish_list = []
    translatedToGerman_list = []

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
        translation = gt.translate_text_with_model('de', tweet_extended, model="nmt")
    
        #adding the translated tweets to the list 'translatedToEnglish'
        translatedToGerman_list.append(translation)

        # adding the English tweets to the originalEnglish_list
        originalEnglish_list.append(tweet_extended)





    return  originalEnglish_list, translatedToGerman_list
