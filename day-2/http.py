import httplib
import json
from datetime import datetime
from click._compat import raw_input

print "\n\nThis API Client fetches posts from https://jsonplaceholder.typicode.com/ API\n\n"

post_id = raw_input("Enter the post ID: ")

connection = httplib.HTTPConnection('jsonplaceholder.typicode.com')
connection2 = httplib.HTTPConnection('jsonplaceholder.typicode.com')
connection3 = httplib.HTTPConnection('jsonplaceholder.typicode.com')

connection.request("GET", "/posts/" + post_id)
posts = connection.getresponse()
print "\nSuccessfuly Connected - ", posts.status, posts.reason, "\n"

connection2.request("GET", "/posts/" + post_id + "/comments")
comments = connection2.getresponse()

data = json.loads(posts.read())
data2 = json.loads(comments.read())

id = data['id']
title = data['title']
body = data['body']
userId = data['userId']

c_name = data2[0]['name']
c_email = data2[0]['email']
c_msg = data2[0]['body']

connection3.request("GET", "/users/" + str(userId))
user = connection3.getresponse()
data3 = json.loads(user.read())

u_name = data3['name']
username = data3['username']
u_email = data3['email']
u_phone = data3['phone']
u_website = data3['website']

print "Post ID:", id, "\n\nTitle:", title, "\n\nBody:", body, "\n\nWritten By:", u_name, "\n\nAuthor Email:", u_email, "\nAuthor Phone:", u_phone, "\nAuthor Website:", u_website, "\n\nComments:", c_msg, "\nCommenter:", c_email, 


connection.close()