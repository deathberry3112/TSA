from textblob import TextBlob
import streamlit as st
import tweepy
st.set_page_config(layout="wide",page_title="Sentimental analysis")

st.title('Twitter Sentimental Analysis')

api_keys = '1uce35bPTuyHOskDB9tShr2fk'
api_secret_keys = 'vfluYWaZzvgltkHy7R7wWcSeKj9DgRk7EtvPvwN80GoWzXgoFa'
access_token = '1465622947406614530-POB1JrtDZBrtONwf4zwBzEpkN5Pk3Z' 
access_token_secret = 'Tjcy1r2LS52CgULKCKBBO0wK9NviRffkw5miAUdbHhepL'

auth_handler = tweepy.OAuthHandler(consumer_key=api_keys, consumer_secret=api_secret_keys)
auth_handler.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth_handler)

search_term=st.text_input('Enter the topic to be analysed ')

tweet_amount = st.number_input('Tweets:')

tweets=tweepy.Cursor(api.search_tweets, q=search_term ,lang= 'en').items(tweet_amount)

polarity=0


positive=0
negative=0
neutral=0
st.subheader("Tweets to be analysed")
for tweet in tweets:
    final_text =  tweet.text.replace('RT' ,'')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    if final_text.startswith('@'):
        position = final_text.index('')
        final_text = final_text[position+2:]
    anaylsis = TextBlob(final_text)
    tweet_polarity = anaylsis.polarity 
    if tweet_polarity > 0.00:
        positive += 1
    elif tweet_polarity < 0.00:
        negative += 1
    elif tweet_polarity == 0.00: 
        neutral += 1 
    polarity += tweet_polarity 
    st.write(final_text)   


print(polarity)
st.subheader('Result of analysed tweets:')
st.write(f'Amount of positive tweets:{positive}')
st.write(f'Amount of negative tweets:{negative}')
st.write(f'Amount of neutral tweets:{neutral}')


