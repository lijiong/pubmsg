<template>
    <div>
        <p>{{username}}</p>
        <div v-for="topic in topic_list">
            <span> {{topic.title}} </span>
	    <button v-on:click="add_topic(topic)">add</button>
            <div  v-for="t in topic.topic_list">
                <span v-on:click="open_topic(t)"> {{t.title}} </span>
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        data() {
            return {
                username : 'lijiong',
                topic_list : ''
            }
        },
        mounted() {
            this.topic_list = [{'title':'a', 'topic_list':[{'title':'a-1'}, {'title':'a-2'}]}, {'title':'b', 'topic_list':[]}];
	    this.$http.get('http://api.pubmsg.com/api/topic/all').then((res)=>{
                console.log(res);
            });
        },
        methods:{
            open_topic(topic){
                console.log('open topic ' + topic.title + ' ...');
                this.$router.push('/topic');
            },
            add_topic(topic){
                console.log('open topic ' + topic.title + ' ...');
                this.$router.push('/new_topic');
            }
        }
    }
</script>
