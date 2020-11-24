package com.testing.business.msg.application;

import com.testing.business.msg.domain.Topic;

import java.util.ArrayList;

/**
 * Created by lijiong on 2020/11/11.
 */
public class SharedNote {
    static class Book {


    }

    void init() {
        //create book topic
        registerTopic("topic.book", Book.class);
    }

    long createUser() {

    }

    void updateUser() {

    }

    long createGroup() {

    }

    void updateGroup() {

    }

    long createBook(String name) {
        Book book = new Book(name);
        Topic topic = new Topic();
        topic.userList = new ArrayList<Long>();

        messageAgent.createTopic(book);
    }

    long listBook() {
        return messageAgent.searchTopic(accountId);
    }

    void updateBook() {

    }

    long createNote() {

    }

    long updateNote() {

    }







}
