<template>
    <div>
      <h2>Login to Foodiology</h2>
      <form @submit.prevent="login">
        <label for="username">Username:</label>
        <input type="text" v-model="username" required>
  
        <label for="password">Password:</label>
        <input type="password" v-model="password" required>
  
        <button type="submit">Login</button>
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
      login() {
        // You can add login logic here, for now, just log the credentials
        console.log('Login with:', this.username, this.password);
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add component-specific styles if needed */
  form {
    max-width: 300px;
    margin: 20px auto;
    padding: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
  }
  
  button {
    background-color: #fabbe0;
    color: white;
    padding: 10px;
    border: none;
    cursor: pointer;
  }
  </style>
  