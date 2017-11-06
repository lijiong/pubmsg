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

### case1:im
#### 1V1
post message topic:<u1-u2>

pull topic:<u1-u2>

#### nVn
create topic1 perm:rw(u1,u2,u3,u4) 
post message topic1
pull topic1
list topic range:() /time off num
return nextoff

#### get my topic list
permlist

### case2:bbs
#### create topic 
post topic sub-topic

#### create sub topic

#### create a message
post topic message

#### create a reply
post message message

#### list topic

#### list message

#### list reply

### case3:twitter

#### create self topic

#### post a message

#### subscribe a topic
create super_topic
post super_topic topic

#### list feed
pull super_topic
























