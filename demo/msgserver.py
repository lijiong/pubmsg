import sqlite3

class MesssageServer:

    def get_conn(self):
        conn = sqlite3.connect('pubmsg.db')
        return conn

    def __init__(self, ):
        conn = sqlite3.connect('pubmsg.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE user 
             (uid integer, username text, passwd text, PRIMARY KEY(uid ASC), UNIQUE(username))''')
        c.execute('''CREATE TABLE group
             (gid integer, group_name text, PRIMARY KEY(gid ASC))''')
        c.execute('''CREATE TABLE group_item
             (gid integer, uid integer, PRIMARY KEY(gid, uid))''')
        c.execute('''CREATE TABLE message 
             (mid integer, title text, content text, PRIMARY KEY(mid ASC))''')
        c.execute('''CREATE TABLE topic 
             (tid integer, title text, perm text, PRIMARY KEY(tid ASC))''')
        c.execute('''CREATE TABLE topic_item
             (tid integer, type integer, item_id integer, PRIMARY KEY(tid, type, iterm_id))''')
        conn.commit()
        conn.close()

    def gen_uniqid():
        return long(time.time() * 1000) * 1000 + random.randint(0, 1000)

    def user_create(self, username, pri_key, user_extension) :
        c = conn.cursor()
        uid = gen_uniqid()
        c.execute('''INSERT INTO user (uid, username, passwd) values (?, ?, ?)''', ())
        conn.commit()
        conn.close()
        return uid

    def session_create(self, username, token):
        c = conn.cursor()
        sid = gen_uniqid()
        expire_time = time.time()
        d
        c.execute('''INSERT INTO session (uid, sid, expire_time) values (?, ?, ?)''', (uid, sid, expire_time))
        conn.commit()
        conn.close()
        return uid


    def user_group_create(self, group_name):
        c = conn.cursor()
        gid = gen_uniqid()
        c.execute('''INSERT INTO group (gid, group_name) values (?, ?)''', (gid, group_name))
        conn.commit()
        return gid

    def message_create(self, user_id, title, content, topic_list):
        c = conn.cursor()
        mid = gen_uniqid()
        c.execute('''INSERT INTO message (mid, title, content) values (?, ?)''', (mid, title, content))
        conn.commit()
        return mid

    def topic_create(self, user_id, perm_list, title):
        c = conn.cursor()
        mid = gen_uniqid()
        c.execute('''INSERT INTO topic (tid, title) values (?, ?)''', (tid, title))
        conn.commit()
        return mid

    def message_query(self, topic_id, last_message_id):
        c = conn.cursor()
        c.execute('''SELECT mid, title, content FROM message WHERE tid = ?''', (topic_id,))
        row = c.fetchone()
        message_list = 
        while row is not None:
            message = {'mid':row[0], 'title':row[1], 'content':row[2]}
            message_list.append(message)
            row = c.fetchone()
       return message_list

    def topic_status(self, topic_id, last_message_id):
        c = conn.cursor()
        c.execute('''SELECT count(*) FROM message WHERE tid = ?''', (topic_id,))
        topic_count = cur.fetchone()[0]

        c.execute('''SELECT count(*) FROM message WHERE tid = ? AND mid > ?''', (topic_id, last_message_id))
        topic_count_from_last = cur.fetchone()[0]
        return (topic_count, topic_count_from_last)
        
    def topic_children_status(self, topic_id, last_message_id):

    def user_serach(self, keyword):
         
class IMClient:
    def __init__(self):
        self.client = MessageClient()

    def create_account(self, username):
        uid = client_.user_create(username, passwd, pub_info, pri_info)
        self.client_.topic_create("%s_root" % (username, ), {'rw':[uid]})

    def login(self):
        self.client_.create_session(username, passwd)
        self.client_.topic_children_status()

    def find_user(self, username):
        client_.user_search(username)

    def add_friend(self, user_id): 
        if user_id < self.user_id_:
            topic_name = "talk_%d_%d" % (user_id, self.user_id_)
        else :
            topic_name = "talk_%d_%d" % (self.user_id_, user_id)
        client_.topic_create(topic_name, {"rw":[user_id, self.user_id_]})

    def send_message(self, topic_id, title, content): 
        topic_id = ''
        client_.message_create(topic_id, title, content) 

    def create_group_chat(self, user_id_list): 
        client_.topic_create(topic_name, {"rw":user_id_list})

    def topic_list(self):
        client_.list_topic(self.root_topic_id)

    def topic_status(self, topic_id):
        last_message_id = client_.topic_user_tag(topic_id)  
        client_.topic_status(topic_id, last_message_id)

    def poll_message(self, topic_id):
        message_data = client_.message_query(topic_id_list, last_message_id) 
        local_.save_message(message_data)

    def topic_view(self, topic_id):
        local_.message_query(topic_id, conf.once_read_num)


class TwitterClient:
    def user_create(self, username):
        self.client.create_user(username, passwd)

    def user_login(self, username): 
        self.client.create_key(username, passwd)

    def post_message(self, content): 
        title = ''
        self.client.post(title, content, '%d_post' % (self.uid,)) 

    def del_message(self, message_id)

    def feed_add(self, username): 
        self.client.topic_add('%d_feed' % (self.uid,), '%d_post' % (uid,))

    def feed_remove(self, username): 
        self.client.topic_del('%d_feed' % (self.uid,), '%d_post' % (uid,))

    def feed_view(self):
        self.client.topic_view('%_feed' % (self.uid,))

    def get_new_feed_count(self):
 
    def search_message(self, keywords):

    def message_in_topic(self, topic, rank):


class ForumClient:




