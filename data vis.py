'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob

import matplotlib
matplot.lib.use('TkAgg')
import matplotlib.pylot as plt


# from wordcloud import wordcloud
#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity[]
subjectivity[]
# Continue your program below!



ls=[], []
for each in tweetData:
    tb= TextBlob(each["text"])
    ls[0].append (tb.polarity)
    ls[1].append(tb.subjectivity)
    print subjectivity
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
