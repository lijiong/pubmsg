# pubmsg
a public message system, can be used as bbs, im, twitter, blog, feed, etc.

## command
pubmsg support some commands, blow:
### post
post a message, a message is a json data, must contain some field:

{
   "username":"james",
   "token":"c4ab534513248863fe",
   "title":"", //optional
   "content":"hello",
   "topic":["", ""]
}

{
   "message_id":"M01112132"
}

### view

view a topic, a sub topic or a message.


### get

get message-id  return message content.
{
   "username":"james",
   "title":"",
   "content":"",
   "topic":[]
}

### list

list topic-id sort by time/weight
return messageid or topicid under this topic.

{
    "list": [
       "t123132131223123",
       "m124312321432535",
    ]
}

## application

http://xxx/view/t123








