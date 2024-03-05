 <template>
    <div>
      <h2 class="title">Login to Foodiology</h2>
      <form @submit.prevent="login" class="login-form">
        <label for="username">User</label>
        <input type="text" v-model="username" required>
  
        <label for="password">Password:</label>
        <input type="password" v-model="password" required>
  
        <button type="submit">Login</button>
      </form>
      <router-link to="/create-account" class="create-account-link">Create an Account</router-link>
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


/* ... existing styles ... */



  /* Add component-specific styles if needed */
  .title {
    text-align: center;
    color: #333;
  }
  
  .login-form {
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
    background-color: #6bd4d3;
  }
  
  .create-account-link {
    display: block;
    text-align: center;
    margin-top: 20px;
    color: #333;
    text-decoration: none;
    font-weight: bold;
  }
  </style>
   