import nltk                                 # Python library for NLP
from nltk.corpus import twitter_samples     # Sample twitter dataset from nltk
import matplotlib.pyplot as plt             # Library for visualization
import random                               # pseudo-random number generator
import re                                   # library for regular expression operations
import string                               # for string operations
from nltk.corpus import stopwords           # module for stop words that come with NLTK
from nltk.stem import PorterStemmer         # module for stemming
from nltk.tokenize import TweetTokenizer    # module for tokenizing strings

# nltk.download('twitter_samples')

# Selecting the set of positive and negative tweets
all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')
print('Number of positive tweets: ', len(all_positive_tweets))
print('Number of negative tweets: ', len(all_negative_tweets))
print('The type of all positive tweets is: ', type(all_positive_tweets))
print('The type of a tweet entry is: ', type(all_negative_tweets[0]))

# Declare a figure with a custon size
fig = plt.figure(figsize=(5, 5))

# Print positive in 'green' color
print('\033[92m' + all_positive_tweets[random.randint(0, 5000)])
# Print negative in 'green' color
print('\033[91m' + all_negative_tweets[random.randint(0, 5000)])

# # Labels for the two classes
# labels = 'Positive', 'Negative'
#
# # Sizes for each slide
# sizes = [len(all_positive_tweets), len(all_negative_tweets)]
#
# # Declare pie-chart, where the slices will be ordered and plotted counter-clockwise
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
#
# # Equal aspect ratio ensures that pie is drawn as  a circle
# plt.axis('equal')
#
# # Display the chart
# plt.show()

# Our selected sample. Complex enough to exemplify each step
tweet = all_positive_tweets[2277]
print("Printing tweet:", tweet)

# Download the stopwords from NLTK
# nltk.download('stopwords')

print('\033[92m' + tweet)
#print('\033[94m')

# remove old style retweet text "RT"
tweet = re.sub(r'^RT[\s]+', '', tweet)

# remove hyperlinks
tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

# remove hashtags
# only removing the # sign from the word
tweet = re.sub(r'#', '', tweet)

# Printing the clean tweet
print(tweet)

# Instantiate tokenizer class
tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)

# tokenize tweets
tweet_tokens = tokenizer.tokenize(tweet)
print('Tokenized string:')
print(tweet_tokens)

# Import the English stop word list from NLTK
stopwords_english = stopwords.words('english')
print('Stop words')
print(stopwords_english)

print('Punctuation')
print(string.punctuation)

clean_tweet = []

for word in tweet_tokens:
    if word not in stopwords_english and word not in string.punctuation:
        clean_tweet.append(word)

print('List after removing stop word and punctuations:')
print(clean_tweet)

# Instantiate stemming class
stemmer = PorterStemmer()

# Create an empty list to store the stems
tweet_stem = []

for word in clean_tweet:
    stem_word = stemmer.stem(word)
    tweet_stem.append(stem_word)

print('Stemmed Words:')
print(tweet_stem)

# Preprocessing ends here

















