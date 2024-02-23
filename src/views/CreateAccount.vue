<template>
    <div>
      <h2 class="title">Create an Account</h2>
      <form @submit.prevent="create" class="create-form">
        <label for="username">Username:</label>
        <input type="text" v-model="username" required>
  
        <label for="password">Password:</label>
        <input type="password" v-model="password" required>
  
        <button type="submit">Create</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      create() {
        // You can add login logic here, for now, just log the credentials
        console.log('Create with:', this.username, this.password);
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add component-specific styles if needed */
  .title {
    text-align: center;
    color: #333;
  }
  
  .create-form {
    max-width: 400px;
    margin: 20px auto; 
    padding: 25px;
    border: 1px solid #ccc;
    border-radius: 15px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  label {
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
  }
  
  input {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px; 
    box-sizing: border-box;
  }
  
  button {
    background-color: #f792ac;
    color: white;
    border-radius: 5px;
    padding: 10px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #ba3850;
  }
  </style>
   