import facebook
from datetime import datetime
import time
from random import choice

# Generate access token at https://developers.facebook.com/tools/explorer
access_token = 'users-access-token'

graph = facebook.GraphAPI(access_token, version = '2.5')

thankyou_comments = ['Thanks a lot', 'Thank you!', 'Thanks']

birthday_keywords = ['happy', 'birthday', 'bday', 'wish', 'returns', 'b\'day']

args = {'fields' : 'birthday'}
birthdate = datetime.strptime(graph.get_object('me', **args)['birthday'], '%m/%d/%Y')

birthdate_this_year = datetime(datetime.now().year, birthdate.month, birthdate.day)
birthdate_unix_timestamp = int(time.mktime(birthdate_this_year.timetuple()))

args = {'since' : birthdate_unix_timestamp, 'limit': 500}
birthday_posts = graph.get_connections('me', 'feed', **args)

for birthday_post in birthday_posts['data']:
    comment = choice(thankyou_comments)
    graph.put_object(birthday_post['id'], 'likes')
    graph.put_object(birthday_post['id'], 'comments', message = comment)


