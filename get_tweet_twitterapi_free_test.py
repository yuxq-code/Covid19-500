# get timeline tweet (including statue and reply)

import pandas as pd
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterPager

screen_name = 'amazon'
api = TwitterAPI("Ifk7sehmvoZ2XMQffLMNLN4e8",
                 "SBWW9hIe4q9F1bhiv2Oawbkp8ggKoQgDKFVw7pApgFXppwQRCM",
                 "1682624094-6VoIGahlnATPk7vqFxRUnJcusJBCgCxZinEJWvs",
                 "HbReSBQ5AIQUr7vdflXaIj2mRoom4ALjguepbE2nZWKue")


def get_all_tweets(screen_name):
    pager = TwitterPager(api, 'statuses/user_timeline', {'screen_name': screen_name, 'count': 200})
    alltweets = pager.get_iterator(wait=3.5)
    outtweets = [
        [screen_name, tweet['id_str'], pd.to_datetime(tweet['created_at']), tweet['text'], tweet['retweet_count'],
         tweet['user']['location'], tweet['favorite_count'], tweet['truncated'], tweet['is_quote_status'],
         tweet['lang'], tweet['place']] for tweet in alltweets]

    df = pd.DataFrame(outtweets, columns=['user_name', 'id', 'time', 'text', 'retweets', 'geo', 'favorite_count',
                                          'truncated', 'quoted', 'language', 'test'])

    df.to_csv(str(screen_name) + '.csv', index=False)
    print('finish')


if __name__ == '__main__':
    get_all_tweets('amazon')