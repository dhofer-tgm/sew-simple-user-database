<template>
  <div class="hello">
    <h1>Simple User Database</h1>

    <h2>Login:</h2>
    <div class="input-group">
      <input type="text" class="form-control" placeholder="email" v-model="email">
      <input type="password" class="form-control" placeholder="password" v-model="password">
      <div class="input-group-apppend">
        <button class="btn btn-outline-accept" v-on:click="getStudents()" id="">Send!</button>
      </div>
    </div>

    <h2>Users:</h2>
    <table class="table">
      <thead>
      <tr>
        <th scope="col">Picture</th>
        <th scope="col">Email</th>
        <th scope="col">Username</th>
        <th scope="col"></th>
      </tr>
      </thead>
      <tbody id="tbody">
      <tr>
        <td>
          <label class="btn">
            <img v-bind:src="url" style="width:50px; border-radius: 50%" alt="">
            <input type="file" id="addStudentFile" v-on:change="updatePreviewImage()" accept=".png,.jpg,.jepg"
                   style="display: none">
          </label>
        </td>
        <td><input type="email" name="email" class="form-control" id="addStudentEmail" v-model="addStudentInput.email"
                   placeholder="Enter email"></td>
        <td><input type="text" name="username" class="form-control" id="addStudentUsername"
                   v-model="addStudentInput.name" placeholder="Enter username"></td>
        <td>
          <div class="btn-group" role="group" aria-label="Basic example">
            <button type="button" v-on:click="addStudent()" id="createStudentButton" class="btn btn-success">Upload</button>
            <button type="button" class="btn btn-danger">Cancel</button>
          </div>
        </td>
      </tr>
        <Student v-bind:id="'student-'+index" v-for="(student, index) in students" v-bind:student="student" v-bind:index="index"></Student>
      </tbody>
    </table>
  </div>
</template>

<script>
  import axios from 'axios'
  import Student from '@/components/Student'
  import EditStudent from '@/components/EditStudent'
  import { EventBus } from '../event-bus.js'
  import Vue from 'vue'

  export default {
    name: 'HelloWorld',
    data() {
      return {
        students: null,
        url: 'https://mdbootstrap.com/img/Photos/Others/placeholder-avatar.jpg',
        addStudentInput: {
          name: '',
          email: '',
          picture: ''
        },
        email: 'admin@userdb.com',
        username: '',
        password: 'admin'
      }
    },
    components: {
      'Student': Student,
      'EditStudent': EditStudent
    },
    mounted() {
      EventBus.$on('updateStudent', index => {
        var ComponentClass = Vue.extend(EditStudent)
        var instance = new ComponentClass({
            propsData: { student: this.students[index], index:index, parent:this }
        });
        instance.$mount();
        var student = document.getElementById('student-'+index);
        student.parentNode.replaceChild(instance.$el,student);
      })
    },
    methods: {
      getStudents() {
        const path = /*window.location.hostname+*/process.env.BACKEND_SERVER;

        axios.get(path, {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          auth: {
              username: this.email,
              password: this.password
            }
        }).then((res) => {
          this.students = res.data;
        }).catch((error) => {
          console.log(error);
          console.log(error.response)
        });
      },
      addStudent: function () {

        var data = new FormData();
        var imagefile = document.querySelector('#addStudentFile');
        data.append('picture', imagefile.files[0]);
        //console.log(imagefile.files[0]);
        data.append('email', this.addStudentInput.email);
        data.append('username', this.addStudentInput.name);

        const path = process.env.BACKEND_SERVER;
        axios.post(path, data, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          auth: {
              username: this.email,
              password: this.password
            }
        }).then((res) => {
          console.log(res);
          this.getStudents();
        }).catch((error) => {
          console.error(error);
        });
      },
      updatePreviewImage: function () {
        var imagefile = document.querySelector('#addStudentFile');
        this.url = URL.createObjectURL(imagefile.files[0]);
      }
    },
    created() {
      //this.getStudents()
    }
  }
</script>
