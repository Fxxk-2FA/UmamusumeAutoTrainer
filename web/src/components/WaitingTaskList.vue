<template>
  <div>
    <div class="card">
      <div class="card-body">
        <div class="d-flex bd-highlight">
          <h5 class="card-title">等待中</h5>
          <span v-on:click="clearList"  class="ml-auto btn auto-btn">清空</span>
        </div>
      </div>
      <TaskList v-bind:task-list="waitingTaskList" v-bind:no-data-label="'无等待中任务'"></TaskList>
    </div>
  </div>
</template>

<script>
import TaskList from "./TaskList.vue"
export default {
  name: "WaitingTaskList",
  props:["waitingTaskList"],
  components: {TaskList},
  methods:{
    clearList:function (){
      this.waitingTaskList.forEach(t => {
        let payload = {
          task_id: t.task_id
        }
        console.log(JSON.stringify(payload))
        this.axios.delete("/task", JSON.stringify(payload)).then()
      });
    }
  },
  data:function (){
    return{
    }
  }
}
</script>

<style scoped>
  .card-body{
    border-bottom: 1px solid rgba(0,0,0,.125);
  }

</style>