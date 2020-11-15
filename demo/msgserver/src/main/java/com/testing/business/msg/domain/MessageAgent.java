package com.testing.business.msg.domain;

/**
 * Created by lijiong on 2020/11/11.
 */
public class MessageAgent {
    public void postMessage(Message msg) {
        rep.saveMessage(msg);
    }

    public void createTopic(Topic topic) {

    }

    public void queryMessage() {

    }

    public void pullMessage() {

    }
}
