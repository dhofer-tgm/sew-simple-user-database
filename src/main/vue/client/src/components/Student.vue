<template>
  <tr v-bind:id="'student-'+index">
    <td v-bind:id="index+'-picture'"><img width="50px" style="border-radius: 50%;"
                                          v-bind:src="'data:image/jpeg;base64,'+student.picture"/></td>
    <td v-bind:id="index+'-email'">{{ student.email }}</td>
    <td v-bind:id="index+'-username'">{{ student.username }}</td>
    <td>
      <div class="btn-group" v-bind:id="index+'-buttons'" role="group" aria-label="Basic example">
        <button type="button" class="btn btn-warning" v-on:click="updateStudent()">Edit</button>
        <button type="button" class="btn btn-danger" v-on:click="deleteStudent()">Delete</button>
      </div>
    </td>
  </tr>
</template>

<script>
  import { EventBus } from '../event-bus.js'
  import axios from 'axios'
  export default {
    name: 'Student',
    props: ['student', 'index'],
    methods: {
      updateStudent: function () {
        EventBus.$emit('updateStudent', this.index);
      },
      deleteStudent: function () {
        const path = process.env.BACKEND_SERVER+'&email='+this.student.email;
        console.log(path)
        console.log('username: ' + this.$parent.email)
        console.log('password: ' + this.$parent.password)
        axios.delete(path, {
          auth:{
            username: this.$parent.email,
            password: this.$parent.password
          }
        }).then((res) => {
          console.log(res);
          this.getStudents();
        }).catch((error) => {
          console.error(error);
        });
      },
    }
  }
</script>
