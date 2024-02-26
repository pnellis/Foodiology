<template>
  <div id="app">
    <header class="navigation-header">
      <!-- <h1>Foodiology</h1> -->
      <img :src="Logo" alt="Foodiology Logo" class="logo"/>
      <img src="@/assets/foodiology.png" alt="Foodiology Logo" class = "logo">
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/">Community</router-link>
        <router-link to="/AboutUs">About Us</router-link>
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
html, body, #app {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}

.logo {
  margin-left: 20px;
  margin-right: 20px; /* Add some space between the logo and navigation links */
  width: auto;
  height: 75px;
}

#app {
  font-family: 'Arial', sans-serif;
  text-align: center;
  /* padding: 20px; */
}

.navigation-header {
  display: flex; /* Use flex display to align items in a row */
  align-items: center; /* Align items to the start of the flex container */
  background-color: #ffffff;
  color: rgb(134, 212, 208);
  width: 100%;
  padding: 10px 0;
  height: 100px;  
  /* OR use min-height if you want it to be able to grow in certain conditions */
}


nav {
  display: flex;
  justify-content: space-around;
  flex-grow: 1; /* Allow the navigation to fill the remaining space */
}

nav a {
  text-decoration: none;
  color: rgb(134, 212, 208);
  font-size: 25px;
  font-weight: bold;
}


nav a:hover {
  color: #6bd4d3; /* Change the color to your preferred hover color */
}

main {
  margin-top: 20px;
}


/* footer {
  margin-top: 20px;
  padding: 10px;
  background-color: #f1f1f1;
} */

/* Responsive design for smaller screens */
@media (max-width: 768px) {
  .logo {
    height: 80px; /* Smaller logo for mobile */
  }

  header {
    padding: 15px 0; /* Less padding on mobile */
  }

  nav {
    padding: 0 10px; /* Less padding on mobile */
  }

  nav a {
    font-size: 0.9em; /* Smaller font size for mobile */
  }
}
</style>
