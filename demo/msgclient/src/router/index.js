import Vue from 'vue'
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'

import Login from '@/views/login/login.vue'
import Main from '@/views/main/main.vue'
import Topic from '@/views/topic/topic.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/main',
      name: 'Main',
      component: Main 
    },
    {
      path: '/topic',
      name: 'Topic',
      component: Topic
    }
  ]
})
