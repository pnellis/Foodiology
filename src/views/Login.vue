<template>
    <div>
      <h2>Login to Foodiology</h2>
      <form @submit.prevent="login">
        <label for="username">Username:</label>
        <input type="text" v-model="username" required>
  
        <label for="password">Password:</label>
        <input type="password" v-model="password" required>
  
        <button  type="submit">Login</button>
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
    max-width: 400px;
    margin: 20px auto; 
    padding: 25px;
    border: 1px solid #ccc;
    border-radius: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 20px;
  }
  
  input {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px; 
    text-align: center;
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
  