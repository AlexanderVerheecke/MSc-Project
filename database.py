import psycopg2


"""
Class for everything concerning the databases connecting through psycopg2. 
The database must be stored locally with this parameter. 

Inserts into the following databases:
- english
- german
- englishtranslation
- germantranslation
"""

print('Connecting to the PostgreSQL database...')

#CONNECT TO THE tweets DATABASE 

con = psycopg2.connect(
    host = "localhost",
    database = "tweets",
    user = "",
    password = ""
    )

"""
# ======== SQL COMMANDS USED FOR DATABASE CREATION & EXPORTING TO EXCEL ===================================================

# CREATE DATABASE tweets;

# CREATE TABLE english (                   <-- insert from originalEnglish_list           
#      tweet_number Serial,
#      tweet text
#  );

# CREATE TABLE german (                 <-- insert from originalGerman_list    
#      tweet_number Serial,
#      tweet text
#  );

# CREATE TABLE  englishTranslation(           <-- insert from translatedToEnglish_list
#      tweet_number Serial,
#      tweet text
#  );

# CREATE TABLE  germanTranslation(           <-- insert from translatedToGerman_list
#      tweet_number Serial,
#      tweet text
#  );

# DURING EXPORTING TO CSV FILES SOMETIMES ENCODING NOT PROPER, NEED TO MANUALLY REPLACE STUFF LIKE '&amp;' to & in csv files

# \COPY (select * from english) TO '/Users/alex/Documents/GitHub/TwitterSentimentAnalysis/CSV/English.csv' DELIMITER ',' CSV HEADER;
# \COPY (select * from germantranslation) TO '/Users/alex/Documents/GitHub/TwitterSentimentAnalysis/CSV/GermanTranslation.csv' DELIMITER ',' CSV HEADER;
# \COPY (select * from englishtranslation) TO '/Users/alex/Documents/GitHub/TwitterSentimentAnalysis/CSV/EnglishTranslation.csv' DELIMITER ',' CSV HEADER;
# \COPY (select * from german) TO '/Users/alex/Documents/GitHub/TwitterSentimentAnalysis/CSV/German.csv'  DELIMITER ',' CSV HEADER;

# =============================================================================================================================
"""

#CREATE A CURSOR WHICH WILL BE USED TO COMMUNICATE WITH THE DATABASE
cursor = con.cursor()


#  Adds the English tweets to the database
def addIntoDatabaseENGLISH(insertTweet):

    con = psycopg2.connect(
    host = "localhost",
    database = "tweets",
    user = "",
    password = ""
    )
    cursor = con.cursor()

    cursor.execute('INSERT INTO english (tweet) VALUES (%s)', (insertTweet,))

    con.commit()
    
    cursor.close()

    con.close()

#  Adds the English transaltion to the database
def addIntoDatabaseENGLISH_TRANSLATION(insertTweet):

    con = psycopg2.connect(
    host = "localhost",
    database = "tweets",
    user = "",
    password = ""
    )
    cursor = con.cursor()

    cursor.execute('INSERT INTO englishtranslation (tweet) VALUES (%s)', (insertTweet,))

    con.commit()
    
    cursor.close()

    con.close()


#   Adds the German tweets to the database
def addIntoDatabaseGERMAN(insertTweet):

    con = psycopg2.connect(
    host = "localhost",
    database = "tweets",
    user = "",
    password = ""
    )
    cursor = con.cursor()

    cursor.execute('INSERT INTO german (tweet) VALUES (%s)', (insertTweet,))

    con.commit()
    
    cursor.close()

    con.close()

#   Adds the German transaltion to the database
def addIntoDatabaseGERMAN_TRANSLATION(insertTweet):

    con = psycopg2.connect(
    host = "localhost",
    database = "tweets",
    user = "",
    password = ""
    )
    cursor = con.cursor()

    cursor.execute('INSERT INTO germantranslation (tweet) VALUES (%s)', (insertTweet,))


    con.commit()
    
    cursor.close()

    con.close()



#COMMITING EVERYTHING BEFORE CLOSING
con.commit()

#CLOSING THE CURSOR AFTER QUERY IS COMPLETE
cursor.close()

#CLOSE THE CONNECTION TO THE DATABASE
con.close()
