<template>
  <div id="app">
    <header>
      <!-- <h1>Foodiology</h1> -->
      <img :src="Logo" alt="Foodiology Logo" class="logo"/>
      <img src="@/assets/foodiology.png" alt="Foodiology Logo" class = "logo">
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/login">Login</router-link>
        <!-- Add more navigation links as needed -->
      </nav>
    </header>

    <main>
      <router-view></router-view>
    </main>

    <footer>
      <!-- Add footer content if needed -->
    </footer>
  </div>
</template>

<script>
import Logo from '@/assets/logo.png';
import foodiology from '@/assets/foodiology.png';
export default {
    
    data() {
      return {
        Logo: Logo,
        foodiology: foodiology
      };
  
      
    },
    
  };
</script>

<style>
.logo {
  width: auto; /* Adjust the width to your preferred size */
  height: 100px; /* Maintain the aspect ratio */
}
#app {
  font-family: 'Arial', sans-serif;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

header {
  background-color: #f792ac;
  color: white;
  padding: 20px;
}

nav {
  display: flex;
  justify-content: space-around;
  margin-top: 10px;
}

nav a {
  text-decoration: none;
  color: white;
  font-weight: bold;
}

main {
  margin-top: 20px;
}

footer {
  margin-top: 20px;
  padding: 10px;
  background-color: #f1f1f1;
}
</style>
