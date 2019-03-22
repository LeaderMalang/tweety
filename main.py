import tweepy as tw
import csv
import time
consumer_key= '#'
consumer_secret= '#'
access_token= '#'
access_token_secret= '#'


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# tweet = api.get_status('572342978255048705')
# print(tweet.text)

# Do the reading
file1 = open('test.csv', 'r')
reader = csv.reader(file1)
new_rows_list = []
for row in reader:
    tweet = api.get_status(row[0])
    new_row = [row[0], row[1], tweet.text]
    new_rows_list.append(new_row)
    time.sleep(3)
file1.close()   # <---IMPORTANT

#Do the writing

file2 = open('test2.csv', 'wb')
writer = csv.writer(file2)
writer.writerows(new_rows_list)
file2.close()



