
# TwitterSentimentAnalysis

This is the repo for my UoB 2022 project. The idea of the project is the creation of a sentiment analysis application enabling the analysis of sentiment from German tweets using various models, and comparing the results to the sentiment classification of the exact same German data but translated to English and classified with an English model and vice versa. The aim is to see how strongly machine translations such as Google Translate translate the sentiment or if this is lost. 

The following is an explanation of the classes found in the folder:

1. tweetRetrieval.py: This is the main class. When running the class, the user is asked to enter the number of tweets to analyse, the keyword to search for, and the language. If the language is English (en), it calls englishTweets.py to convert the tweets into a list of English tweets as well as translate the tweets using googleTranslate.py and insert it into a German translation list. It does the same when the language is German, inserting tweets into a German list and an English list. It then calls database.py to insert the tweets into their corresponding PostgreSQL database locally stored.

2. database.py: Accesses the locally stored SQL database to insert the tweets into their corresponding database

3. englishTweets.py: Takes the tweets, and stores them into an English and German translation list with gogoleTranslate.py

4. germanTweets.py: Takes the tweets, and stores them in a German and English translation list with googleTranslate.py

5. googleTranslate.py: Makes use of Google's translate_v3 API to automatically translate the tweets. If called with a lot of tweets, this stage takes a long time and will sometimes stop in the middle

After all tweets were scraped and translated, they needed to be hand-labelled. Following this, we trained models on DAI and SemEval and used these models to perform on the scrapped tweets under OwnTweets below.

This project made extensive use of the following datasets:
- DAI: de_sentiment_UNIQUE.csv
- SemEval: SemEval2017_DataSet.csv
- OwnTweets: 
    - German: latestGerman.csv as well as latestEnglishTranslatedToGERMAN.csv
    - English: latestEnglish.csv as well as latestGermanTranlatedToEnglish.csv
- MBERT COMBINED: Train_data_GERandENG_SHUFFLED.csv (this is a combination of DAI and SemEval used to train M-BERT)

This repo also includes colab ipynb files for the machine learning and neural network models:
- Traditional_Machine_Learning_Models.ipynb:  Includes the machine learning models
- English_LSTM.ipynb: Includes the English LSTM model
- German_LSTM.ipynb: Includes the German LSTM model
- MBERT_model.ipynb: Includes the Multilingual BERT model

Instructions on how to use each individual colab file can be found at the top of each indiviual project's colab site.
